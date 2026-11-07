# Session 2026-11-04: AI video model research and pricing for claudiaplessl.at

## 1. Best AI video model / is Seedance 2.5 the latest? (/last30days run)

- **Seedance 2.5** is ByteDance's newest model (released 2026-07-31): 30 s single pass with audio, up to 50 references. No official Seedance 3.0 / 2.6. Sites selling "Seedance 3.0" are third-party.
- **It is not the newest model overall.** Kling 4.0 (Kuaishou) launched globally in mid-October 2026. Early reviews are mostly disappointed; it's best used for editing.
- **There is no single best model.** Artificial Analysis ranks Wan 3.0 (Alibaba) first. LLM Stats ranks Kling v3 first (no 2.5/4.0 rows yet). Polymarket: Google at 96% for best text-to-video at end of November; image-to-video MiniMax 49%, Google 41%.
- **Gemini Omni** (Google) replaced Veo 3.1 as the Gemini default. "Omni 1.5" is not a confirmed release. Sora is shut down (API off 2026-09-24).
- Raw research file: `~/Documents/Last30Days/best-ai-video-generation-model-raw-v3.md` (web supplements appended).

## 2. Cheapest way to make several 30 s videos from claudiaplessl.at

**Website:** Mag. Claudia Plessl, interior design and organizing coaching, Vienna / Lower Austria. German, calm and airy, sage green and rosé. Usable references: hero image, portrait, four-step process. No real before/after photos yet.

**Higgsfield pricing (read live at higgsfield.ai/pricing on 2026-11-04, EUR excl. VAT)**
- Starter €19 (270 credits), Plus €59 monthly / €47 annual (1,200 credits), Ultra €129 monthly / €99 annual (3,000 credits).
- Seedance 2.5 "unlimited" lasts only 7 days. On Plus it's annual-only (720p); on Ultra monthly it's 720p; on Ultra annual it's 1080p.
- Business plans: Team €65 per seat, Scale €150 per seat (annual). Scale has 30-day unlimited Seedance 2.5, but clips are capped at 25 s / 720p and business verification is required. Too expensive for a single user.
- Credit costs per second (Higgsfield blog, 2026-10-30): Seedance 2.5 uses 3 / 7 / 16 credits at 480p / 720p / 1080p, so a 30 s clip costs 90 / 210 / 480 credits. Kling 4.0 uses 2.75 / 4 credits at 720p / 1080p.

**Wan 3.0 (Alibaba, closed weights, max 30 s)**
- Model Studio list price per second: standard $0.05 / $0.10 / $0.20 (480p / 720p / 1080p), so a 30 s clip costs $1.50 / $3.00 / $6.00. The page shows a "limited-time 30% off". Prime tier: $0.068 / $0.14 / $0.28 per second.
- 30 s free quota on Model Studio, and failed generations aren't billed.
- Also available via OpenRouter (`alibaba/wan-3.0`), but not on its EU-only routing, so data goes to Alibaba Cloud International.

**Seedance 2.5 via API (BudgetPixel):** about $6.94 per 30 s at 720p, about $15.60 at 1080p (OpenRouter / BytePlus).

**Recommendation**
1. Draft with Wan 3.0 at 480p, render only the good ones at 720p or 1080p. About $45 for 15 clips at 720p.
2. If the quality isn't good enough: one month of Higgsfield Ultra **monthly** (€129) and do all the work within the 7 unlimited days. Avoid annual plans.

**Refined recommendation (later in session)**
- First flag: no real before/after photos. AI-generated "transformations" presented as Claudia's work would be misleading advertising. Stick to mood, process and brand clips.
- Don't upload the portrait to Alibaba without Claudia's written consent; use the hero image for tests.
- Leave out generated speech (German lip-sync unverified); add an Austrian German voiceover and text overlays in post.
- Expected cost: under €50 on the Wan path, €129 at most on the Higgsfield fallback.

## 3. Registering for Wan 3.0 (Alibaba Cloud Model Studio, international)

1. Create the account at alibabacloud.com (not aliyun.com, the mainland-China edition). A third-party guide says the international edition skips identity verification.
2. Model Studio console: `bailian.console.alibabacloud.com`, region **Singapore (ap-southeast-1)**. Keys, endpoints and model lists are separate per region.
3. Model ID `wan3.0-video` (plus `wan3.0-video-prime`) is in the official model list: 480p/720p/1080p, 2–30 s, 30 fps.
4. API key: `https://modelstudio.console.alibabacloud.com/ap-southeast-1/settings/api-key` → Create API Key (default workspace, All permissions). Copy it immediately; it's shown only once and doesn't expire. Store it as `DASHSCOPE_API_KEY` in a secrets file, never in chat.
- Not verified: payment method requirements; whether the international account can actually activate Wan 3.0 (an older forum report says only Qwen was available); current per-second price and free quota.
- Docs: https://www.alibabacloud.com/help/en/model-studio/get-api-key · https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-api-reference

## 4. MCP options for Wan 3.0 in Claude Code

- **No official Alibaba MCP server for video.** The `aliyun/*` MCP servers (agent-toolkit, ops, RDS and others) are for cloud operations. The official MCP registry has nothing for Wan.
- **AceDataCloud WanMCP** (third-party, hosted) supports `wan3.0-video`. Untested setup command: `claude mcp add --transport http --scope user wan https://wan.mcp.acedata.cloud/mcp`, then `claude mcp login wan`. Downsides: an extra data processor (jurisdiction and data-protection terms unchecked), billing in AceDataCloud credits (EUR conversion unknown), and possibly public HTTPS image URLs only.
- **Own small MCP server** (FastMCP) against the official API is possible. Data goes only to Alibaba.

## 5. Claude Code skills for Wan 3.0 (GitHub search)

- **Recommended: `modelstudioai/cli`** ("Official Model Studio CLI", Apache-2.0, v2.8.2 released 2026-11-04). Install with `npm install -g bailian-cli`, then `bl skill init`. Its `bailian-gen` skill uses `wan3.0-video` for `bl video generate` / `bl video ref`, plus TTS (`cosyvoice-v3-flash`) and image generation. Local files upload automatically; video jobs run in the background (`--download`).
  - International account: generating with an API key works. Console/MCP/account features are China-site only (README).
  - To check: telemetry/update checks and the `BAILIAN_CALLER_*` attribution variables. Also `bl auth login --api-key <KEY>` puts the key in shell history, so look for a safer method in `bl auth login --help`. Avoid the `curl | bash` installer unless it's read first.
- Alternatives: `QwenCloud/qwencloud-ai` `qwencloud-video-generation` (Python, accepts `DASHSCOPE_API_KEY`; Wan 3.0 support not checked) is the fallback. Skip `aliyun/alibabacloud-aiops-skills` (Wan 2.6 only, manages keys on its own) and `AceDataCloud/Skills` (third party). The community prompt skills (`wubin1836/ai-hive-*`, `yeisme/scaena-skills`, `2799662352/ai-image-master`) are for reading only.

## Open items / not verified

- Whether Higgsfield's individual-plan unlimited mode allows full 30 s clips.
- German speech and lip-sync quality in Wan 3.0 and Seedance 2.5.
- Whether Wan's 30% discount is still active; EUR/USD conversion not done.
- GDPR: using Claudia's portrait on Alibaba Cloud International. Need her written consent first.
- Wan 3.0 activation on the international account, and payment requirements.
- `bailian-cli` telemetry and safe API-key login.

## Next steps (waiting for the user)

**Most likely to cause trouble:** step 1.4. If Wan 3.0 can't be activated on the international account, steps 2 and 3 are pointless.

### Step 1: Register and create an API key (user)

1. Open https://www.alibabacloud.com (not aliyun.com) and click Free Trial / Sign Up. Check: you can sign in, and the top bar shows the English-language international console.
2. Add a payment method if asked (credit card or PayPal; which ones are accepted is unconfirmed).
3. Open https://bailian.console.alibabacloud.com and set the region in the top right to **Singapore (ap-southeast-1)**. Check: "Singapore" is shown in the top right.
4. In the Model Plaza, search for `wan3.0-video` and open the model page. Check: the model can be activated, the price per second is shown, and the free 30 s quota is listed. **If it's missing or locked, stop and tell Claude; the Wan plan has to change.**
5. Open https://modelstudio.console.alibabacloud.com/ap-southeast-1/settings/api-key and click Create API Key (default workspace, All permissions), then OK.
6. Copy the key immediately (it's shown only once) and save it on nuc8 without it appearing on screen or in shell history:
   ```bash
   mkdir -p ~/.config/secrets && chmod 700 ~/.config/secrets
   read -rsp 'DashScope key: ' K && printf 'export DASHSCOPE_API_KEY=%s\n' "$K" > ~/.config/secrets/dashscope.env && unset K
   chmod 600 ~/.config/secrets/dashscope.env
   ```
   Check: `ls -l ~/.config/secrets/dashscope.env` shows `-rw-------`. Never paste the key into the chat.
7. Tell Claude "key is ready" and whether step 4 worked.

### Step 2: Install and check `bailian-cli` (Claude, after the user's OK)

Undo: `npm uninstall -g bailian-cli` and remove the installed skills (Claude notes where `bl skill init` puts them).

1. Check the prerequisites: `node --version`, `npm --version`. Check: both exist; if not, ask before installing Node.
2. Look at the package before installing: `npm view bailian-cli version maintainers repository`. Check: the repository is `github.com/modelstudioai/cli` and the version is 2.8.2 or newer.
3. Install: `npm install -g bailian-cli`. Check: `bl --version` prints the version.
4. Read the help and settings: `bl --help`, `bl auth login --help`, `bl video generate --help`, plus any config or telemetry options. Check: report what is sent where, and how to turn telemetry off if possible.
5. Log in without the key ending up in shell history (read it from standard input or the environment, if `--help` offers a way). If there's no safe way, stop and ask. Check: a free test such as a model list or auth status works against Singapore.
6. Install the skills: `bl skill init`. Check: show where the skill files ended up, and read `bailian-gen` and `bailian-protocol` before using them.
7. Write the result into `session.md`.

### Step 3: One 480p test clip from the hero image (together)

1. Claude takes the hero image URL from claudiaplessl.at and shows the image (it has no people, so no portrait problem).
2. The user confirms the motif and prompt. Draft: a calm camera move through the bright room, sage green and rosé accents, no text, no people, no audio.
3. Claude shows the exact command first, then the user approves it: roughly `bl video generate` with `--model wan3.0-video`, the image, 480p, 30 s, no audio and `--download`. The exact flags depend on `--help` from step 2. Cost: free quota, otherwise about $1.50.
4. Claude starts the job, waits for it and downloads the MP4 into the project folder. Check: the file plays, and `ffprobe` shows 854×480 at the requested length.
5. The user reviews it: does it fit the calm, airy brand? Any warped furniture, flicker, or unwanted text?
6. Decide what's next. Good: plan the remaining clips at 480p, then render the keepers at 720p. Not good: one more attempt with a better prompt, or switch to the Higgsfield fallback.
7. Claude adds the result and the actual cost to `session.md`.

---

# Session 2026-11-07: Public repository setup

## Completed

1. Initialized `/home/nuc8/05_development/44_video` as a Git repository with default branch `main`.
2. Created the public GitHub repository [AINxtGenDev/video](https://github.com/AINxtGenDev/video).
3. Configured `origin` as `git@github.com:AINxtGenDev/video.git` and set `main` to track `origin/main`.
4. Configured this repository's SSH command to use `/home/nuc8/.ssh/github_werner`, with `IdentitiesOnly=yes` and `StrictHostKeyChecking=yes`. Confirmed that the key authenticates as `AINxtGenDev`. Repository creation used the existing GitHub CLI login; Git pushes used the specified SSH identity.
5. Created [readme.md](readme.md) with the project purpose, status, proposed workflow, SSH setup, credential handling, and references.
6. Created [.gitignore](.gitignore) to exclude local `.env` files, private-key file patterns, `.claude/`, dependencies, caches, logs, and generated assets in `outputs/` and `renders/`.
7. Committed and pushed the initial three files (`readme.md`, `.gitignore`, and `session.md`) in commit [`8c4c4e8`](https://github.com/AINxtGenDev/video/commit/8c4c4e88d995a49fa0fcd81d1672142e09ff12c8), titled `Initialize video project with README and research notes`.

## Verification

- GitHub reported public visibility and default branch `main`.
- The local commit and remote `main` matched after the initial push; the working tree was clean.
- `git check-ignore` confirmed that `.env` and `.claude/` were ignored. Only the three intended project files were tracked.
- The staged changes passed `git diff --cached --check`.

## Current status and next steps

- The project remains in the planning stage. No provider integration was installed and no video-generation job was submitted during this session.
- The 4 November research above remains historical and unverified. Recheck current primary sources before relying on model names, availability, prices, technical capabilities, or legal conclusions.
- Provider activation, credential setup, CLI review, and the first approved test clip remain pending as described above.
- User workflow preference: keep `session.md` updated with completed work, decisions, verification, and outstanding items; commit and push completed updates automatically. Review the staged content for secrets before publishing to this public repository.

## Sources

- [Public project repository](https://github.com/AINxtGenDev/video).
- [Initial commit and tracked files](https://github.com/AINxtGenDev/video/commit/8c4c4e88d995a49fa0fcd81d1672142e09ff12c8).
- Local verification: `gh repo view`, `git status`, `git remote -v`, `git config --local --get core.sshCommand`, `git ls-files`, `git ls-remote`, and `git check-ignore`.

## README presentation update — 7 November 2026

- User preference: the README should be colorful and include icons and emojis.
- Updated [readme.md](readme.md) with amber, purple, teal, and blue Shields.io badges, an emoji title and section headings, and a workflow table with visual stage markers.
- Preserved the project status, SSH instructions, credential guidance, and references. Clarified that this log includes subsequent project updates as well as the original research.
- Badges use externally hosted images from `img.shields.io`; descriptive alternative text and adjacent text links keep the information available without the images.

## Wan 3.0 through OpenRouter — planning, 7 November 2026

- Requested a plan to use `alibaba/wan-3.0` with the OpenRouter credential intended to be stored in the project's `.env`.
- Confirmed the exact model through the public [video catalog](https://openrouter.ai/api/v1/videos/models). Use the dedicated asynchronous video API, with submit, poll, and download operations.
- Prepared [wan-openrouter-plan.md](wan-openrouter-plan.md) and supporting [primary-source research](wan-openrouter-research.md); linked both from the README.
- Local checks: Python 3.12.3 and `ffprobe` are available; `.env` has permissions `0600` and remains ignored. No `OPENROUTER_API_KEY` assignment was found. Requested only the variable name or local addition of that assignment; no credential value was displayed or transmitted.
- Proposed first generation: five seconds, 480p, 16:9, audio disabled, generic interior prompt. Base generation estimate USD 0.25; USD 0.2125 with the currently advertised 15% discount. These are estimates, not a billing guarantee. [Model pricing](https://openrouter.ai/alibaba/wan-3.0).
- The current model page reports no EU in-region route, and OpenRouter excludes video generation from ZDR eligibility. Use a generic prompt initially and verify data handling before uploading client assets. [Video retention documentation](https://openrouter.ai/docs/guides/overview/multimodal/video-generation#zero-data-retention).
- No authentication test, dependency installation, paid generation, or account configuration change was performed. Next: make the OpenRouter credential available, implement and verify the proposed client, then agree on the exact first paid request and budget.

## Session handoff and publication — 7 November 2026

### Completed and published

- README presentation changes were committed and pushed in [`1a5d8d6`](https://github.com/AINxtGenDev/video/commit/1a5d8d689ceaf2c823bfd2b0ac79131140ab2d33).
- The OpenRouter implementation plan, primary-source research, README references, and planning notes were committed and pushed in [`ba2a099`](https://github.com/AINxtGenDev/video/commit/ba2a099c8a8d10f5fe8c053be79cff1899e81872).
- Before that planning commit, the example JSON was parsed and its duration, resolution, and aspect ratio were checked against the live video catalog. Local document links resolved, `.env` was untracked, the publication files passed a credential-pattern check, and `git diff --cached --check` passed.
- After that push, the local and remote `main` commits matched and the working tree was clean.

### Active next steps

1. Make the intended OpenRouter credential available under `OPENROUTER_API_KEY` in the ignored local `.env`, or identify its existing variable name. At the last credential-variable inspection, that assignment was absent; credentials have not been re-inspected for this documentation update.
2. Implement the small local client described in [wan-openrouter-plan.md](wan-openrouter-plan.md), including dry-run, preflight, single submission, resumable polling, protected downloads, and cost reporting.
3. Verify error handling and credential boundaries with mocked responses before any paid request.
4. Agree on the exact prompt and spending limit, then submit the proposed five-second 480p test and record the result and reported cost.

The OpenRouter route is the current implementation plan. The earlier direct-Alibaba account and `bailian-cli` instructions remain historical alternatives; they are not prerequisites for this route. No video client has been implemented and no generation has been submitted.

The user reaffirmed that session information should be updated, committed, and pushed automatically after completed work. This is the working preference for future sessions; no background scheduler or Git hook has been installed.

## First Wan clip generated — 7 November 2026

### Request and reference

- User authorized generating one five-second 480p clip without audio, using the style of `/home/nuc8/05_development/55_laulau/78_plessl-website`, and saving it in this project.
- Inspected the existing `website/public/video/vorstellung.mp4` (58.2 seconds, 1080×1920), sampled its frames, and read the current frame CSS and source notes. Selected its calm portrait presentation, cream canvas, sage/blush palette, natural materials, and restrained movement.
- Used the website's public [living-room image](https://claudiaplessl.at/_next/static/media/projects-living-610.dea2e572.webp) as the first-frame reference. Its downloaded bytes matched `website/src/assets/projects-living-610.webp`. No portrait, voice sample, or full source video was uploaded. The website project was inspected without modifications.

### Authentication and generation

- The earlier credential checks correctly found no named `OPENROUTER_API_KEY` assignment, but a subsequent format-only inspection found one OpenRouter-format token stored as a bare value in `.env`. Loaded that unambiguous token in memory and successfully authenticated with `GET /api/v1/key`. No credential value was displayed or committed; `.env` was not modified.
- Rechecked the live video catalog and provider pricing, then submitted one job to `POST /api/v1/videos` using `alibaba/wan-3.0`, `duration: 5`, `resolution: "480p"`, `aspect_ratio: "9:16"`, `generate_audio: false`, first-frame reference, and `provider.only: ["alibaba"]`.
- Prompt: preserve the reference interior and its cream/sage/blush palette, with an extremely slow push-in and slight parallax; no people, transformations, scene cuts, added text, or new logos.
- Saved the accepted job ID before polling. The job completed; returned `usage.cost` was **USD 0.2125**, with `is_byok: false`. No second generation was submitted.
- **Observed provider deviation:** despite the requested settings, the downloaded result was 640×640, approximately 5.038 seconds, and included an AAC audio track. Future integrations must validate the actual output and enforce delivery requirements locally rather than relying solely on request flags. This observation concerns this job; it does not establish behavior for every Wan request.

### Delivered file and verification

- Final file: `/home/nuc8/05_development/44_video/plessl-wan-5s-480p-silent.mp4`.
- Locally removed audio, trimmed to 150 frames, and placed the complete square interior scene on a 480×854 cream portrait canvas with a thin sage rule, following the source film's restrained presentation. The picture panel is 432×432; this is a portrait composition of the square generation, not a native full-frame portrait generation.
- `ffprobe` verified **5.000 seconds, 480×854, H.264, 30 fps, 150 frames, and exactly one video stream with no audio stream**. File size: **490,601 bytes**.
- SHA-256: `50ea1959749e5427d6cdbf715802ea8e9dc2ba3fcd3c7044bb07104474699652`.
- Full-file FFmpeg decode passed with `-xerror`. Sampled generated frames and the finished preview were visually inspected; user review of the motion and composition remains next.
- Local evidence: `outputs/plessl-wan-5s-480p/request.json`, `job.json`, `provider-original.mp4`, `download.json`, `validation.json`, and preview images. These remain ignored. The final root-level MP4 is explicitly ignored as well.
- Updated the README to reflect the first completed draft. No global dependencies, reusable client, Git hook, or background automation were installed.

### Sources and next step

- Source style: the website project's `video-source/compositions/frames/_shared.css`, `04-ordnung-gestaltung.html`, `website/src/app/globals.css`, existing MP4, and reference asset.
- API: [video catalog](https://openrouter.ai/api/v1/videos/models), [submit reference](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request), and local sanitized job/validation records listed above.
- Next: review the delivered clip before authorizing another generation or a longer/higher-resolution version. A reusable client remains optional future work; the previously missing authentication prerequisite has now been resolved for this execution.
