/* "Suggest an improvement" box at the bottom of every chapter page.
   Suggestions go to a small Cloudflare Worker (worker/feedback-worker.js),
   which files each one as a GitHub Issue. Nothing shows until FEEDBACK_URL is set. */
(function () {
  var FEEDBACK_URL = ""; // e.g. "https://sjo-feedback.YOURNAME.workers.dev"
  if (!FEEDBACK_URL) return;

  function addBox() {
    var section = document.querySelector(".page-inner section.normal");
    if (!section || document.getElementById("sjo-feedback")) return;
    var started = Date.now();
    var chapter = (document.title || "").split(" | ")[0];
    var box = document.createElement("div");
    box.id = "sjo-feedback";
    box.innerHTML =
      '<h3>Suggest an improvement</h3>' +
      '<p>Spotted a mistake, or something that didn’t land? Tell us. No account needed, and we don’t collect your name or email.</p>' +
      '<form>' +
      '<textarea name="message" rows="4" maxlength="3000" required placeholder="What should change on this page?"></textarea>' +
      '<input type="text" name="website" tabindex="-1" autocomplete="off" class="sjo-hp" aria-hidden="true">' +
      '<button type="submit">Send suggestion</button> <span class="sjo-status" role="status"></span>' +
      '</form>';
    section.appendChild(box);
    var form = box.querySelector("form");
    var status = box.querySelector(".sjo-status");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = form.message.value.trim();
      if (msg.length < 10) { status.textContent = "Please write a little more."; return; }
      var btn = form.querySelector("button");
      btn.disabled = true; status.textContent = "Sending…";
      fetch(FEEDBACK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: msg, website: form.website.value,
          page: location.pathname, chapter: chapter, elapsed: Date.now() - started
        })
      }).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        form.message.value = "";
        status.textContent = "Thank you! Your suggestion was sent.";
      }).catch(function () {
        status.textContent = "Sorry, that didn’t send. Please try again later.";
      }).then(function () { btn.disabled = false; });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", addBox);
  else addBox();
})();
