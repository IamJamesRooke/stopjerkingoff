/* Cloudflare Worker: turns "Suggest an improvement" submissions from
   stopjerkingoff.com into GitHub Issues labelled "reader-feedback".

   Secrets (set in the Cloudflare dashboard, never in this repo):
     GITHUB_TOKEN  fine-grained token with Issues: Read and write on
                   IamJamesRooke/stopjerkingoff only.

   Spam protection: honeypot field, minimum time on page, length limits,
   link limit, and only requests from stopjerkingoff.com are accepted. */
const REPO = "IamJamesRooke/stopjerkingoff";
const ORIGINS = ["https://stopjerkingoff.com", "https://www.stopjerkingoff.com"];

function cors(origin) {
  return {
    "Access-Control-Allow-Origin": ORIGINS.includes(origin) ? origin : ORIGINS[0],
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Vary": "Origin",
  };
}

function reply(status, text, origin) {
  return new Response(text, { status, headers: { ...cors(origin), "Content-Type": "text/plain" } });
}

// Stop @mentions and #references from pinging people or linking issues.
function defang(s) {
  return s.replace(/@/g, "@​").replace(/#(\d)/g, "#​$1");
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    if (request.method === "OPTIONS") return new Response(null, { headers: cors(origin) });
    if (request.method !== "POST") return reply(405, "POST only", origin);
    if (!ORIGINS.includes(origin)) return reply(403, "Forbidden", origin);

    let d;
    try { d = await request.json(); } catch { return reply(400, "Bad request", origin); }
    const message = String(d.message || "").trim();
    const page = String(d.page || "/").slice(0, 200);
    const chapter = String(d.chapter || "").slice(0, 120);

    // Bots fill the hidden field or submit instantly; pretend success so they move on.
    if (d.website || Number(d.elapsed) < 4000) return reply(200, "ok", origin);
    if (message.length < 10 || message.length > 3000) return reply(400, "Bad length", origin);
    if ((message.match(/https?:\/\//g) || []).length > 2) return reply(200, "ok", origin);

    const short = message.replace(/\s+/g, " ").slice(0, 60);
    const body = [
      `**Page:** [${defang(chapter) || page}](https://stopjerkingoff.com${page.startsWith("/") ? page : "/" + page})`,
      "",
      "**Suggestion:**",
      "",
      defang(message).split("\n").map((l) => "> " + l).join("\n"),
      "",
      "_Sent anonymously from the website's feedback box._",
    ].join("\n");

    const r = await fetch(`https://api.github.com/repos/${REPO}/issues`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${env.GITHUB_TOKEN}`,
        "Accept": "application/vnd.github+json",
        "User-Agent": "stopjerkingoff-feedback",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: `Reader suggestion: ${chapter ? chapter + " | " : ""}${short}`.slice(0, 200),
        body,
        labels: ["reader-feedback"],
      }),
    });
    if (!r.ok) return reply(502, "Could not file the suggestion", origin);
    return reply(200, "ok", origin);
  },
};
