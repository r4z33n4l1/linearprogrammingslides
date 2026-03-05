# Render Script Context

This directory contains helper scripts for rendering the Manim animations used by the presentation.

The scripts here are intentionally separate from the application routes and UI so an agent can work on animation output without touching the Next.js presentation code.

## File

- `render-animations.sh`: batch wrapper around the Manim scenes in `animations/lp_presentation_animations.py`.

## How `render-animations.sh` Works

The script resolves:

- `ROOT_DIR`: project root
- `MANIM_BIN`: defaults to `./venv/bin/manim`
- `ANIMATION_FILE`: `./animations/lp_presentation_animations.py`
- `QUALITY`: defaults to `-pql`
- `MODE`: first positional argument, defaults to `all`

## Supported Modes

- `core`
  - Renders the most important talk animations only.
  - Order:
    - `LevelSetSweepAnimation`
    - `FeasibleRegionAnimation`
    - `ConvexityAnimation`

- `all`
  - Renders every animation currently defined for the deck.

- `optional`
  - Renders only the lower-priority supporting animations.
  - Order:
    - `BakeryFeasibleRegion`
    - `SimplexPathAnimation`

- Any other argument
  - Treated as a direct scene name and passed to Manim.
  - Example:
    - `./scripts/render-animations.sh LevelSetSweepAnimation`

## NPM Script Mapping

The following `package.json` scripts call into this render layer:

- `npm run render:anim:convexity`
- `npm run render:anim:feasible`
- `npm run render:anim:level-set`
- `npm run render:anim:bakery`
- `npm run render:anim:simplex`
- `npm run render:anim:core`
- `npm run render:anim:all`

## Agent Guidance

- Use the single-scene npm scripts when iterating on one slide.
- Use `render:anim:core` when preparing the deck quickly.
- Use `render:anim:all` only when a full refresh is actually needed.
- If Manim is not installed in `./venv`, set `MANIM_BIN` explicitly before calling the shell script.

Example:

```bash
MANIM_BIN=/path/to/manim QUALITY=-pqh ./scripts/render-animations.sh core
```
