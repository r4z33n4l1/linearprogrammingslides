#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIM_BIN="${MANIM_BIN:-$ROOT_DIR/venv/bin/manim}"
ANIMATION_FILE="$ROOT_DIR/animations/lp_presentation_animations.py"
QUALITY="${QUALITY:--pql}"
MODE="${1:-all}"

if [[ ! -x "$MANIM_BIN" ]]; then
  echo "manim executable not found at $MANIM_BIN" >&2
  echo "Set MANIM_BIN=/path/to/manim or install it in ./venv." >&2
  exit 1
fi

render_scene() {
  local scene="$1"
  echo "Rendering $scene"
  "$MANIM_BIN" "$QUALITY" "$ANIMATION_FILE" "$scene"
}

case "$MODE" in
  core)
    render_scene "LevelSetSweepAnimation"
    render_scene "FeasibleRegionAnimation"
    render_scene "ConvexityAnimation"
    ;;
  all)
    render_scene "ConvexityAnimation"
    render_scene "FeasibleRegionAnimation"
    render_scene "LevelSetSweepAnimation"
    render_scene "BakeryFeasibleRegion"
    render_scene "SimplexPathAnimation"
    ;;
  optional)
    render_scene "BakeryFeasibleRegion"
    render_scene "SimplexPathAnimation"
    ;;
  *)
    render_scene "$MODE"
    ;;
esac
