# Reader feedback box: one-time setup

The "Suggest an improvement" box on every chapter page sends suggestions to a
small Cloudflare Worker, which files each one as a GitHub Issue labelled
`reader-feedback`. Readers need no account. The box stays hidden until step 4.

You need a free Cloudflare account and a GitHub token. It takes about 10 minutes.

## 1. Make a GitHub token (only allowed to create issues)

1. Go to <https://github.com/settings/personal-access-tokens/new>.
2. Name: `stopjerkingoff feedback`. Expiration: 1 year (set a reminder to renew it).
3. Repository access: **Only select repositories**, then pick `IamJamesRooke/stopjerkingoff`.
4. Permissions, then Repository permissions: set **Issues** to **Read and write**. Leave everything else as it is.
5. Click **Generate token** and copy it. Don't paste it anywhere except step 3 below.

## 2. Create the Worker

1. Sign up at <https://dash.cloudflare.com/sign-up> (free plan).
2. In the left menu open **Compute (Workers)**, then **Workers & Pages**, then **Create**, then **Create Worker** ("Hello World").
3. Name it `sjo-feedback` and click **Deploy**.
4. Click **Edit code**, delete everything, paste the whole of
   [`feedback-worker.js`](feedback-worker.js), and click **Deploy**.

## 3. Add the token to the Worker

1. Open the Worker, then **Settings**, then **Variables and Secrets**, then **Add**.
2. Type: **Secret**. Name: `GITHUB_TOKEN`. Value: the token from step 1.
3. Click **Deploy**.

## 4. Switch the box on

Copy the Worker's address (shown on its page, like
`https://sjo-feedback.yourname.workers.dev`) and send it to Claude, or paste it
yourself into `FEEDBACK_URL` at the top of `site/feedback.js` and push.

## Spam protection

The Worker only accepts posts from stopjerkingoff.com. It quietly drops
anything that fills a hidden honeypot field, arrives within 4 seconds of the
page loading, or contains more than two links. It also strips @mentions so
nobody can use it to ping people. If spam still gets through, Cloudflare
Turnstile (free) can be added later.
