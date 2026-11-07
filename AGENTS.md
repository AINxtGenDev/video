# Repository Guidelines

## Project Structure & Module Organization

This repository contains video-production sources and research, rather than a deployed application.

- `introduction-video/`: editable HyperFrames project; `index.html` mounts scenes from `compositions/`.
- `introduction-video/assets/`: website images, brand fonts, and font licenses. Music and Wan footage remain local and ignored.
- `build_source.py`: generates scene HTML and the master; `ledger.json` defines transitions; `finish_wan.sh` completes the Wan export.
- `session.md`: decisions, execution results, verification, and handoff notes. `wan-openrouter-*.md` contain planning and research.
- `outputs/` and root MP4 files: local artifacts excluded from Git.

Before editing video compositions, read the nested [AGENTS.md](introduction-video/AGENTS.md) and [rendering instructions](introduction-video/README.md).

## Build, Test, and Development Commands

Use Node.js 22 and FFmpeg. Run these commands inside `introduction-video/`; package scripts pin HyperFrames 0.9.20:

```bash
npm run check                  # Composition lint, runtime, layout, and contrast checks
npm run dev                    # Interactive preview; remains running
npm run render -- --quality delivery --strict --variables '{"variant":"editorial"}' -o ../plessl-introduction-480p.mp4
bash finish_wan.sh             # Requires both prepared exports; see README
```

A fresh checkout needs the ignored music and Wan media restored locally before checking or rendering. Regenerating with `python3 build_source.py` also requires re-stamping transitions; follow the rendering instructions.

## Coding Style & Naming Conventions

Use four-space Python indentation and two-space indentation for hand-edited HTML/JSON; preserve generated formatting. Use descriptive kebab-case scene names and IDs, such as `portrait` and `contact-domain`. Keep animations deterministic and timelines seekable. HyperFrames provides composition linting; no separate formatter is configured.

## Testing Guidelines

There is no unit-test suite or coverage target. Run `npm run check` after composition changes, inspect scene and transition snapshots, and validate the actual export:

```bash
ffprobe -v error -show_streams -show_format ../plessl-introduction-480p.mp4
ffmpeg -v error -xerror -i ../plessl-introduction-480p.mp4 -f null -
```

Confirm duration, dimensions, streams, readable text, and Claudia's portrait. Preview success alone is insufficient; see [REVIEW.md](introduction-video/REVIEW.md).

## Commit & Pull Request Guidelines

Follow existing imperative commit subjects: `Create`, `Update`, `Record`, or `Add`. Keep commits focused. PRs should explain intent, affected scenes, verification results, and limitations; include review frames and related issue references where applicable. Update `session.md` with completed work and remaining tasks.

## Security & Configuration

Keep credentials, signed download URLs, music, and generated media outside public commits. Parse `.env` as data without displaying secrets. Review staged files and run `git diff --cached --check` before committing. Obtain authorization for paid generation and record reported costs.
