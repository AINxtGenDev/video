# 🎬 Video · AINxtGenDev

**✨ From creative brief to reviewed brand video.**

[![Status: Two Introductions](https://img.shields.io/badge/Status-Two_Introductions-10B981?style=for-the-badge)](#-project-status)
[![Focus: AI Video](https://img.shields.io/badge/Focus-AI_Video-8B5CF6?style=for-the-badge)](#-intended-workflow)
[![Notes: Session Log](https://img.shields.io/badge/Notes-Session_Log-0D9488?style=for-the-badge)](session.md)
[![GitHub: Public Repository](https://img.shields.io/badge/GitHub-Public_Repository-2563EB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AINxtGenDev/video)

AI-assisted video production project for short brand and process videos, initially focused on [claudiaplessl.at](https://claudiaplessl.at).

🌐 **Brand:** [claudiaplessl.at](https://claudiaplessl.at) · 📂 **Repository:** [AINxtGenDev/video](https://github.com/AINxtGenDev/video) · 📝 **Research:** [Session log](session.md)

---

## 🧭 Project status

Two introduction films were completed on **7 November 2026**, using the live website's actual portrait of Claudia, original logo, German text, and soft background music. Both follow the established cream, sage, and blush palette.

| Film | Local file in the project root | Content |
| --- | --- | --- |
| 🌿 Editorial introduction | `plessl-introduction-480p.mp4` | Website imagery, Claudia's portrait, German titles, and music |
| ✨ Wan introduction | `plessl-introduction-wan-480p.mp4` | New `alibaba/wan-3.0` footage, Claudia's actual portrait, titles, and music |

📐 **Both outputs:** 30.000 seconds · 480×854 portrait · 30 fps · H.264 · AAC stereo. Claudia is visible from 5–12 seconds. [Editable source and rendering instructions](introduction-video/README.md).

The earlier silent test remains available locally as `plessl-wan-5s-480p-silent.mp4` (five seconds). The new 20-second Wan source generation reported USD 0.85; the earlier test reported USD 0.2125. [Session notes and verification](session.md).

Videos, music, raw generation responses, and job metadata are retained locally and excluded from this public repository. The editable introduction compositions, public website images, font licenses, and documentation are versioned. A reusable OpenRouter client remains future work.

[session.md](session.md) records the research session dated 4 November 2026 and subsequent project updates, including repository setup on 7 November 2026.

> 🔎 **Research checkpoint:** Treat the provider research as historical. Model availability, pricing, technical capabilities, and legal conclusions require verification against current primary sources before use.

## 🎨 Intended workflow

| Step | Stage | Action |
| --- | --- | --- |
| 1 | 🟣 **Creative brief** | Confirm the brief, source assets, and permission to use them. |
| 2 | 🔵 **Provider review** | Verify availability, current pricing, data handling, and suitable account settings. |
| 3 | 🟢 **Technical setup** | Review the proposed CLI or integration and configure credentials outside Git. |
| 4 | 🟡 **Prompt approval** | Agree on the prompt and spending limit before submitting a generation job. |
| 5 | 🟠 **Draft and review** | Generate a draft, review visual quality, and document the result and actual cost. |
| 6 | 🌸 **Final production** | Produce approved versions and add voiceover, captions, or other finishing elements. |

Detailed proposals and unresolved questions are recorded in [session.md](session.md).

## 💻 Local repository

The initial working directory is `/home/nuc8/05_development/44_video`.

To clone using the project owner's SSH identity:

```bash
git -c core.sshCommand='ssh -i /home/nuc8/.ssh/github_werner -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes' clone git@github.com:AINxtGenDev/video.git
cd video
git config --local core.sshCommand 'ssh -i /home/nuc8/.ssh/github_werner -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes'
```

The key path is specific to that machine. Other contributors should use their own SSH identity and verify GitHub's host key before connecting.

## 🔐 Credentials and generated assets

- 🔑 Keep API credentials in local environment files or an appropriate secrets store. Never commit credentials or private keys.
- 🛡️ `.gitignore` excludes `.env` files, local Claude settings, common dependency/cache directories, and generated files under `outputs/` and `renders/`.
- 🔍 Review staged changes before every commit, especially because this repository is public.
- 🎞️ Keep large generated media outside Git unless a deliberate storage strategy has been selected.

## 📚 References

- [🎬 Wan 3.0 through OpenRouter — implementation plan](wan-openrouter-plan.md).
- [🔎 Wan and OpenRouter — verified API research](wan-openrouter-research.md).
- [Project research and proposed next steps](session.md).
- [GitHub: connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
- [GitHub: ignoring files](https://docs.github.com/en/get-started/git-basics/ignoring-files).

## ⚖️ License

No license has been selected for this project.
