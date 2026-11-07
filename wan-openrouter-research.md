# Alibaba Wan 3.0 through OpenRouter: verified research

Verified on **7 November 2026**, approximately **19:58 UTC**. Only public, read-only requests were made; no credentials were inspected and no generation was submitted. **Observation** means an HTTP response obtained during this investigation; **documentation** means an official published description; **inference** is identified explicitly.

## Result and model discovery

**The exact model `alibaba/wan-3.0` exists in OpenRouter's video catalog.** An unauthenticated GET returned HTTP 200 with 33 models and this exact entry. Its canonical identifier was `alibaba/wan-3.0-20260824`. The filtered general catalog, `GET /api/v1/models?output_modalities=video`, also returned 33 models including this model. Absence from the unfiltered general catalog is therefore insufficient evidence of unavailability. Sources: [live video catalog](https://openrouter.ai/api/v1/videos/models), [filtered live catalog](https://openrouter.ai/api/v1/models?output_modalities=video).

The live video entry exposed:

| Field | Observed value |
| --- | --- |
| `supported_resolutions` | `480p`, `720p`, `1080p` |
| `supported_durations` | Every integer from 2 through 30 seconds |
| `supported_aspect_ratios` | `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `supported_frame_images` | `first_frame`, `last_frame` |
| `generate_audio` | `true` |
| `seed` | `true` |
| `supported_sizes` | `null` |
| `allowed_passthrough_parameters` | Empty array |
| `upscale_factor`, `creativity` | `null` |

These are live catalog declarations, not results of generation tests. Re-query before submitting. The empty passthrough whitelist provides no basis for adding Wan 2.7 options such as `negative_prompt` or `prompt_extend` to Wan 3.0. [Live video catalog](https://openrouter.ai/api/v1/videos/models).

## Pricing and provider

| Resolution | Live catalog SKU, USD/second | Current discounted rate, USD/second | Estimated 10-second clip at discounted rate |
| --- | ---: | ---: | ---: |
| 480p | 0.05 | 0.0425 | 0.425 |
| 720p | 0.10 | 0.085 | 0.85 |
| 1080p | 0.20 | 0.17 | 1.70 |

The catalog uses keys `duration_seconds_480p`, `duration_seconds_720p`, and `duration_seconds_1080p`. The public endpoints response contained one provider, `provider_name: "Alibaba"`, `tag: "alibaba"`, with `pricing.discount: 0.15`. The model page names the provider **Alibaba Cloud Int.**, advertises 15% off, and states a range of $0.0425/second at 480p to $0.17/second at 1080p. The 720p discounted value and clip estimates are arithmetic inferences from the observed rates and discount, not invoices. Do not assume a discount is permanent. [Video catalog](https://openrouter.ai/api/v1/videos/models), [live model endpoints](https://openrouter.ai/api/v1/models/alibaba/wan-3.0/endpoints), [official model page](https://openrouter.ai/alibaba/wan-3.0).

The endpoints response also contains generic text-oriented `supported_parameters`; use the dedicated video catalog and video request schema for video validation. A single listed route provides no evidence of independent provider redundancy. [Live model endpoints](https://openrouter.ai/api/v1/models/alibaba/wan-3.0/endpoints).

Routing semantics: `provider.only` is an allowlist; `order` expresses preference and ordering, rather than by itself proving exclusive use; `ignore` excludes providers. A base provider slug matches its eligible variants and regions, so `{"provider":{"only":["alibaba"]}}` is a provider restriction, not a geographic guarantee. Account restrictions also apply. The general routing guide documents `allow_fallbacks: false` for disabling fallback, but the directly visible video schema specifically identifies `order`, `only`, and `ignore`; prefer the explicit video allowlist for restricting this integration. [Provider-routing documentation](https://openrouter.ai/docs/guides/routing/provider-selection), [video submit schema](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request).

## Documented request and asynchronous workflow

1. Submit JSON to **`POST https://openrouter.ai/api/v1/videos`** with `Authorization: Bearer <API_KEY>` and `Content-Type: application/json`. `model` is required. Supply `prompt` for text-to-video; image-only prompt omission is supported only by models that explicitly permit it. The schema includes `duration`, `resolution`, `aspect_ratio`, `size`, `generate_audio`, `seed`, `frame_images`, `input_references`, `callback_url`, and `provider`. Provider routing accepts `order`, `only`, and `ignore`. `previous_job_id` is restricted to continuation-capable models; Wan support was not established. [Submit API reference](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request).

   A minimal, catalog-compatible **unexecuted** example is:

   ```json
   {
     "model": "alibaba/wan-3.0",
     "prompt": "A static close-up of a ceramic cup with steam rising slowly.",
     "duration": 2,
     "resolution": "480p",
     "aspect_ratio": "16:9",
     "generate_audio": false
   }
   ```

2. Submission returns **HTTP 202**, with required `id`, `polling_url`, and `status`. Persist the returned job ID. Poll **`GET /api/v1/videos/{jobId}`** with Bearer authentication. Required poll fields are `id`, `polling_url`, and `status`; states are `pending`, `in_progress`, `completed`, `failed`, `cancelled`, and `expired`. Optional fields include `error`, `generation_id`, `unsigned_urls`, `urls`, `expires_at`, and `usage`. Usage becomes available after completion and the example includes `cost` and `is_byok`. Treat identifiers as opaque: illustrative job IDs and the documented current ID format differ. [Submit reference](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request), [poll reference](https://openrouter.ai/docs/api/api-reference/video-generation/poll-video-generation-status).

3. After `completed`, download **`GET /api/v1/videos/{jobId}/content?index=0`** with Bearer authentication. The `index` is nonnegative and defaults to zero. Successful content is raw video bytes, documented as `video/mp4`; it is not a JSON response. `unsigned_urls` also require authentication. Optional signed `urls` need no API key and remain usable until `expires_at`; treat those URLs as secrets. [Download reference](https://openrouter.ai/docs/api/api-reference/video-generation/download-generated-video-content), [poll reference](https://openrouter.ai/docs/api/api-reference/video-generation/poll-video-generation-status).

The guide recommends approximately 30-second polling intervals. Frame entries use `{"type":"image_url","image_url":{"url":"https://…"},"frame_type":"first_frame"}`; last-frame entries change `frame_type`. Image references omit `frame_type` and belong in `input_references`. If both image fields are supplied, `frame_images` takes precedence. Seed determinism is not guaranteed. [Video guide](https://openrouter.ai/docs/guides/overview/multimodal/video-generation). The current official image-to-video recipe is [Turn an Image into a Video](https://openrouter.ai/docs/cookbook/video-generation/image-to-video), verified through the official cookbook navigation.

## Retention and European routing

**Video generation is ineligible for Zero Data Retention.** Its asynchronous workflow necessarily retains generated output temporarily; ZDR enforcement blocks routing. BYOK ZDR declarations do not exempt video generation. No fixed output-retention duration for this model was established. [Video guide](https://openrouter.ai/docs/guides/overview/multimodal/video-generation), [ZDR documentation](https://openrouter.ai/docs/guides/features/zdr).

**The model page explicitly states that Wan 3.0 is not currently available through EU in-region routing.** An observed `GET /api/v1/models?output_modalities=video&region=eu` returned HTTP 200 with an empty array. General EU routing is available on Business/Enterprise, uses `eu.openrouter.ai`, and fails rather than falling back outside the region. Its defined Europe boundary includes EU/EEA, the UK, and Switzerland; it is broader than EU-only. Account, billing, authentication, security, and other operational records are outside the payload-residency guarantee. These general controls do not create a European route for Wan. [Model page](https://openrouter.ai/alibaba/wan-3.0), [filtered regional catalog](https://openrouter.ai/api/v1/models?output_modalities=video&region=eu), [in-region routing documentation](https://openrouter.ai/docs/guides/features/in-region-routing).

Provider logging/training policies and OpenRouter's policies are separate. A no-training preference does not establish zero retention. The specific retention period, processing location, contractual terms, and treatment of reference assets for this Wan route remain unverified. [Provider logging documentation](https://openrouter.ai/docs/guides/privacy/provider-logging).

## Operational limits and unresolved items

- No authenticated generation, polling, download, or invoice has been tested; actual account access and enforcement remain unverified.
- No Wan-specific concurrency quota, requests-per-minute quota, prompt length, reference count/size, generated frame rate, or output-retention TTL was established. Generic API errors include 400, 401, 402, 403, 413, 429, and 5xx; avoid interpreting generic example error messages as Wan-specific policy. [Submit reference](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request).
- Audio/video input modalities appear in model metadata, but the request documentation says audio/video references are honored only by supporting providers. The investigated sources do not establish Wan 3.0 reference-media constraints sufficiently to promise audio/video reference behavior. [Model endpoints](https://openrouter.ai/api/v1/models/alibaba/wan-3.0/endpoints), [submit reference](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request).
- Before production use, validate current capabilities, confirm account budgets with `GET /api/v1/key`, bound poll duration and retries, and persist accepted job IDs before further actions. Retrying an uncertain submission could create a second billable job; submission idempotency was not established. Honor `Retry-After` where supplied. These are implementation recommendations, not verified Wan guarantees. [Limits documentation](https://openrouter.ai/docs/api_reference/limits), [official code-first video guide](https://openrouter.ai/blog/tutorials/video-generation-api/).

No alternative model is necessary to resolve exact-model availability: the requested model is documented and catalogued. European-residency or ZDR requirements would require revisiting the service/model choice.
