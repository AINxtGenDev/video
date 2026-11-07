#!/usr/bin/env bash
# Preserve the verified real-portrait sequence in the Wan delivery export.
set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
wan_export="$project_root/outputs/plessl-introduction/wan-export-before-portrait-fix.mp4"
editorial_export="$project_root/plessl-introduction-480p.mp4"
delivery="$project_root/plessl-introduction-wan-480p.mp4"
temporary="$project_root/outputs/plessl-introduction/wan-delivery.tmp.mp4"

test -f "$wan_export"
test -f "$editorial_export"

ffmpeg -hide_banner -loglevel error -y \
  -i "$wan_export" -i "$editorial_export" \
  -filter_complex '[0:v]trim=start=0:end=5,setpts=PTS-STARTPTS[v0];[1:v]trim=start=5:end=12,setpts=PTS-STARTPTS[v1];[0:v]trim=start=12:end=30,setpts=PTS-STARTPTS[v2];[v0][v1][v2]concat=n=3:v=1:a=0[v]' \
  -map '[v]' -map 0:a:0 \
  -c:v libx264 -preset medium -crf 16 -pix_fmt yuv420p -r 30 \
  -c:a copy -movflags +faststart "$temporary"

mv -- "$temporary" "$delivery"
printf 'Finished: %s\n' "$delivery"
