# 🎬 Plan: Wan 3.0 through OpenRouter

Prepared: **7 November 2026**. Scope: implementation planning and public, read-only research. No paid generation or account configuration changes were performed.

## 1. Decision and prerequisites

Use the exact model **`alibaba/wan-3.0`** through OpenRouter's dedicated video API. A public request to `GET /api/v1/videos/models` confirmed this model. Its absence from the ordinary `/models` response does not establish video unavailability. See the [video catalog](https://openrouter.ai/api/v1/videos/models) and [model discovery reference](https://openrouter.ai/docs/api/api-reference/video-generation/list-all-video-generation-models).

For this route, build a small local Python client using OpenRouter authentication; a direct Alibaba account, DashScope key, and Alibaba CLI are outside the proposed implementation. This is a design choice for using the user's existing OpenRouter account, not confirmation that the account can currently generate video.

Local checks:

- Python 3.12.3 and `ffprobe` are available.
- `.env` has permissions `0600` and is ignored by Git.
- No `OPENROUTER_API_KEY` assignment was found. The key value was not displayed, and no other service's credential was used.

**Required before authentication:** add `OPENROUTER_API_KEY` to `.env` using a local editor, or identify its existing variable name. Do not paste the value into chat, commands, documentation, or commits. Parse `.env` as data with `python-dotenv`; do not execute it with shell `source`. Require an explicit credential source and reject empty or conflicting values.

## 2. Preflight without generation

Implement `check` to:

1. Load the credential in memory and call authenticated `GET https://openrouter.ai/api/v1/key`. Report only authentication success and relevant budget/restriction information; never dump the complete response. This endpoint describes the current key, not a guarantee of provider availability or successful billing. [Current-key API](https://openrouter.ai/docs/api/api-reference/api-keys/get-current-api-key).
2. Fetch the video catalog, find the exact model, and validate each requested option. The observed catalog supports integer durations **2–30 seconds**, **480p / 720p / 1080p**, five aspect ratios (**16:9, 4:3, 1:1, 3:4, 9:16**), first/last frames, and an audio-generation option. Refresh these values before submission. [Live video catalog](https://openrouter.ai/api/v1/videos/models).
3. Check current pricing and available account controls. Recommend a dedicated project key with an initial **USD 5 budget** and one job at a time; do not change account settings automatically. A local estimate is not a provider-enforced spending cap. [Spend controls](https://openrouter.ai/docs/guides/best-practices/spend-controls).

Pass condition: authenticated key, model present, supported request, and sufficient applicable budget. Stop with an actionable message on authentication, payment, model, or policy failures.

## 3. First request: a short, silent draft

Start with text-to-video to verify the integration without uploading client assets. Proposed request body, **for review only**:

```json
{
  "model": "alibaba/wan-3.0",
  "prompt": "A calm, airy interior with soft natural daylight, sage green and rose accents, and a slow, subtle camera push-in. Stable furniture geometry and realistic materials. No people, no text, no logos, no scene cuts.",
  "duration": 5,
  "resolution": "480p",
  "aspect_ratio": "16:9",
  "generate_audio": false,
  "provider": {
    "only": ["alibaba"]
  }
}
```

Use `POST https://openrouter.ai/api/v1/videos`, with the key in the HTTPS `Authorization: Bearer …` header and JSON content type. The submit API returns an asynchronous job response. Do not send a chat-completion request. Restrict routing to the observed `alibaba` provider; that restriction does not establish geography. Omit provider passthrough options: the observed Wan catalog advertises none. [Submit API](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request), [video catalog](https://openrouter.ai/api/v1/videos/models), [provider routing](https://openrouter.ai/docs/guides/routing/provider-selection).

Default behavior must be a **dry run** that displays the request and estimate. A distinct `submit` operation starts the paid job only after the prompt and spending limit have been agreed, consistent with the existing project workflow.

## 4. Cost envelope

The live catalog lists base rates of USD 0.05 / 0.10 / 0.20 per second for 480p / 720p / 1080p. The model page currently advertises a 15% discount. The following are calculated generation estimates, excluding taxes, funding fees, currency conversion, and additional attempts. Recheck before spending. [Catalog](https://openrouter.ai/api/v1/videos/models), [model pricing](https://openrouter.ai/alibaba/wan-3.0).

| Clip | Base estimate | With the observed 15% discount |
| --- | ---: | ---: |
| 5 s · 480p | USD 0.25 | USD 0.2125 |
| 30 s · 480p | USD 1.50 | USD 1.275 |
| 30 s · 720p | USD 3.00 | USD 2.55 |
| 30 s · 1080p | USD 6.00 | USD 5.10 |

Use the base rate for the local preflight budget estimate rather than assuming the discount persists. Record returned `usage.cost` as the reported generation charge; account billing remains authoritative. Do not assume Alibaba's direct-service free quota or refund rules apply to OpenRouter.

## 5. Submit once, resume, and download

Implementation requirements:

1. Save the validated request locally under ignored `outputs/<run-id>/`. Atomically persist the returned job ID immediately after acceptance.
2. Poll `GET /api/v1/videos/{jobId}` approximately every 30 seconds, with bounded backoff for transient GET failures. Handle `completed`, `failed`, `cancelled`, and `expired` as terminal states. Use a 20-minute local deadline as an initial operational setting, not a provider SLA. [Polling API](https://openrouter.ai/docs/api/api-reference/video-generation/poll-video-generation-status).
3. A local timeout must preserve the job ID for `resume`; it does not imply cancellation or absence of charges. Do not automatically retry an ambiguous POST: a lost response can leave a running, billable job.
4. On completion, download from `GET /api/v1/videos/{jobId}/content?index=0`. Only send the key to the exact trusted HTTPS API origin. Validate polling/content URLs and handle redirects explicitly so credentials cannot reach an external storage host. Never publish signed download URLs. [Content API](https://openrouter.ai/docs/api/api-reference/video-generation/download-generated-video-content).
5. Stream to a temporary file and rename after success. Save sanitized job status, request metadata, reported cost, and a SHA-256 checksum. Keep sensitive prompts, assets, raw responses, and media in ignored output storage.

The API documents polling, result content, and `usage.cost`; resumability, deadlines, atomic writes, and credential-boundary checks are implementation safeguards proposed here. [Video generation guide](https://openrouter.ai/docs/guides/overview/multimodal/video-generation).

## 6. Validate, then use the hero image

Check the MP4 with `ffprobe`: decoding, actual dimensions, approximately five-second duration, aspect ratio, and absence of an audio stream. Review camera motion, flicker, furniture geometry, text artifacts, and brand fit. Do not hardcode 854×480 or a frame rate that the selected route has not guaranteed.

After the smoke test, select and approve the actual website hero image. Use the documented `frame_images` object with `type: "image_url"`, `frame_type: "first_frame"`, and `image_url.url` pointing to an approved, directly downloadable asset. Verify image access and rights first; do not publish a private asset to GitHub merely to obtain a URL. [Image-to-video cookbook](https://openrouter.ai/docs/cookbook/video-generation/image-to-video).

Review the image-based short draft before requesting a 30-second 480p version. Generate a 720p or 1080p version only after approving the composition and revised budget. A new generation at a higher resolution can differ from the draft; it is not guaranteed to reproduce the same scene.

## 7. Data handling

The model page currently reports **no EU in-region route**. If EU-only processing is required, this plan cannot satisfy that requirement as verified today. OpenRouter's intermediary role does not establish the underlying provider's retention or processing location. Review the actual route and applicable terms before sending client material; begin with the generic prompt above. [Wan model page](https://openrouter.ai/alibaba/wan-3.0), [in-region routing](https://openrouter.ai/docs/guides/features/in-region-routing), [data collection](https://openrouter.ai/docs/guides/privacy/data-collection).

**Video generation is ineligible for OpenRouter Zero Data Retention (ZDR).** Do not disable an existing account privacy requirement to make this route work. A fixed retention period for this route has not been established. [Video retention documentation](https://openrouter.ai/docs/guides/overview/multimodal/video-generation#zero-data-retention), [ZDR policy](https://openrouter.ai/docs/guides/features/zdr).

Keep portraits and other personal or confidential material outside the initial integration test; establish the necessary permissions and data-handling arrangements before expanding its scope.

## 8. Proposed implementation deliverables and verification

Create a small `scripts/wan_video.py` client with `check`, `dry-run`, `submit`, and `resume` operations, plus a project-local virtual environment and reviewed dependency versions. Store request examples without credentials. No MCP server, web application, global CLI installation, or webhook service is needed for this first version.

Before a paid test, use mocked HTTP responses to verify missing credentials, unsupported parameters, cost-limit rejection, ambiguous submission failure, all documented terminal states, resumability, and redirect handling without credential leakage. Then perform the single approved five-second smoke test, record its job ID and actual reported cost, and update `session.md`.

**Current result:** the public integration path is verified; account authentication and generation are pending. This plan does not install dependencies or execute the proposed client.
