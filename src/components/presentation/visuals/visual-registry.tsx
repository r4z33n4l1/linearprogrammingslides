import { BakeryIconVisual } from "./bakery-icon-visual";
import { ConvexityVisual } from "./convexity-visual";
import { ConstraintLinesVisual } from "./constraint-lines-visual";
import { FeasibleRegionVisual } from "./feasible-region-visual";
import { VerticesVisual } from "./vertices-visual";
import { LevelSetVisual } from "./level-set-visual";
import { BakeryGridVisual } from "./bakery-grid-visual";
import { BakeryRegionVisual } from "./bakery-region-visual";
import { HypercubeVisual } from "./hypercube-visual";
import { LPWildVisual } from "./lp-wild-visual";
import { HalfspaceVisual } from "./halfspace-visual";
import { ConvexityHalfspaceVisual } from "./convexity-halfspace-visual";
import { Simplex3DVisual } from "./simplex-3d-visual";
import { BigPictureVisual } from "./big-picture-visual";
import { DualityVisual } from "./duality-visual";

const registry: Record<string, React.FC<{ revealStep?: number }>> = {
  "bakery-icon": BakeryIconVisual,
  convexity: ConvexityVisual,
  "constraint-lines": ConstraintLinesVisual,
  "feasible-region": FeasibleRegionVisual,
  vertices: VerticesVisual,
  "level-set": LevelSetVisual,
  "bakery-grid": BakeryGridVisual,
  "bakery-region": BakeryRegionVisual,
  hypercube: HypercubeVisual,
  "lp-wild": LPWildVisual,
  halfspace: HalfspaceVisual,
  "convexity-halfspace": ConvexityHalfspaceVisual,
  "simplex-3d": Simplex3DVisual,
  "big-picture": BigPictureVisual,
  duality: DualityVisual,
};

export function SlideVisual({ id, revealStep }: { id: string; revealStep?: number }) {
  const Component = registry[id];
  if (!Component) return null;
  return <Component revealStep={revealStep} />;
}
