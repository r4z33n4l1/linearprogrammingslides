# Presentation Rendering Context

This project has two distinct presentation layers:

- Next.js routes for browsing slide prompts and deck structure
- Manim scenes for the small subset of slides that need actual animation

## Separation of Concerns

- `src/` and `app/`
  - Own the web presentation UI.
  - Show prompts, deck organization, and navigation.

- `animations/`
  - Own slide-specific Manim scenes.
  - These are not generic helpers. They map directly to named presentation slides.

- `scripts/`
  - Own command wrappers for rendering those scenes consistently.

## Animated Slide Priority

- Critical
  - Slide 10: `LevelSetSweepAnimation`

- High
  - Slide 7: `FeasibleRegionAnimation`

- Medium
  - Slide 4: `ConvexityAnimation`

- Optional
  - Slide 12: `BakeryFeasibleRegion`
  - Slide 14: `SimplexPathAnimation`

## Typical Workflow

1. Update or inspect the scene in `animations/lp_presentation_animations.py`.
2. Render one scene with the matching npm script.
3. Use `render:anim:core` when preparing the essential deck visuals.
4. Keep generated video output separate from source edits.

## Commands

```bash
npm run render:anim:level-set
npm run render:anim:core
npm run render:anim:all
```

## Maintenance Rule

If a new animation scene or render mode is added:

1. Update `animations/README.md`
2. Update `scripts/README.md`
3. Update this file if priority or workflow changes
