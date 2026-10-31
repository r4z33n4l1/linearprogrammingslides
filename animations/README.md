# Animation Context

This directory is intentionally separate from the Next.js UI code.

It contains Manim scenes for the specific presentation slides that benefit from motion rather than static HTML or image-generation prompts.

## File

- `lp_presentation_animations.py`: the Manim source for the slide-specific animations.

## Scene Map

- `ConvexityAnimation`
  - Slide: 4
  - Purpose: shows the difference between convex and non-convex sets by drawing points and the connecting segment.
  - When to use: when the speaker wants the definition of convexity to land visually instead of verbally.

- `FeasibleRegionAnimation`
  - Slide: 7
  - Purpose: builds the feasible region from constraints and then marks the vertices.
  - When to use: when introducing how inequalities carve out the polygon.

- `LevelSetSweepAnimation`
  - Slide: 10
  - Purpose: shows why the optimum occurs at a vertex by sweeping parallel level sets across the feasible region.
  - When to use: this is the highest-priority animation and the main geometric justification for the theorem.

- `BakeryFeasibleRegion`
  - Slide: 12
  - Purpose: graphs the bakery constraints and highlights the real bottlenecks.
  - When to use: optional worked-example animation after the theorem is established.

- `SimplexPathAnimation`
  - Slide: 14
  - Purpose: gives a closing visual for simplex moving along edges in higher dimensions.
  - When to use: optional closing context, not core to the proof.

## Output Expectations

Default renders use low quality preview settings (`-pql`) for fast iteration.

Manim will place outputs under the standard `media/` tree unless the command is changed.

## Editing Guidance

- Keep these scenes focused on one slide each.
- Do not mix Next.js or React logic into this directory.
- Prefer readable scene names that match slide intent.
- If a new animation is added, update this file and the render script context in `scripts/README.md`.
