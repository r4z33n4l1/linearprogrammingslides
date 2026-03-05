/* ── Slide type system ── */

export type TitleSlide = {
  template: "title";
  title: string;
  subtitle: string;
};

export type AgendaSlide = {
  template: "agenda";
  title: string;
  items: string[];
};

export type Bullet = {
  text: string;
  color?: string;
  bold?: boolean;
  step?: number;
};

export type ContentVisualSlide = {
  template: "content-visual";
  title: string;
  subtitle?: string;
  bullets: Bullet[];
  visualId: string;
  visualStep?: number;
  footer?: string;
};

export type MathSlide = {
  template: "math";
  title: string;
  subtitle?: string;
  rows: { equation: string; annotation: string; step?: number }[];
  footer?: string;
};

export type FullVisualSlide = {
  template: "full-visual";
  title: string;
  visualId: string;
  caption?: string;
  totalSteps?: number;
};

export type TheoremSlide = {
  template: "theorem";
  label: string;
  title: string;
  statement: string;
  notes?: { text: string; bold?: boolean; step?: number }[];
};

export type TableSlide = {
  template: "table";
  title: string;
  subtitle: string;
  columns: string[];
  rows: { cells: string[]; highlight?: boolean }[];
  footer?: string;
};

export type SlideData =
  | TitleSlide
  | AgendaSlide
  | ContentVisualSlide
  | MathSlide
  | FullVisualSlide
  | TheoremSlide
  | TableSlide;

export type Slide = {
  id: string;
  number: number;
  data: SlideData;
};

/** Returns the max step value for a slide (0 if no steps). */
export function getSlideSteps(slide: Slide): number {
  const { data } = slide;
  if (data.template === "content-visual") {
    const bulletMax = data.bullets.reduce((m, b) => Math.max(m, b.step ?? 0), 0);
    return Math.max(bulletMax, data.visualStep ?? 0);
  }
  if (data.template === "math") {
    return data.rows.reduce((m, r) => Math.max(m, r.step ?? 0), 0);
  }
  if (data.template === "full-visual") {
    return data.totalSteps ?? 0;
  }
  if (data.template === "theorem" && data.notes) {
    return data.notes.reduce((m, n) => Math.max(m, n.step ?? 0), 0);
  }
  return 0;
}

/* ── Presentation metadata ── */

export const presentationMeta = {
  title: "Linear Programming: The Geometry of Optimal Decisions",
  course: "MAT392",
  duration: "~15 minutes",
  totalSlides: 13,
};

/* ── Slide content ── */

export const slides: Slide[] = [
  {
    id: "title",
    number: 1,
    data: {
      template: "title",
      title: "Linear Programming:\nThe Geometry of\nOptimal Decisions",
      subtitle: "MAT392",
    },
  },
  {
    id: "roadmap",
    number: 2,
    data: {
      template: "agenda",
      title: "Roadmap",
      items: [
        "A Motivating Example",
        "Convexity",
        "The LP Setup",
        "The Fundamental Theorem",
        "Worked Example",
      ],
    },
  },
  {
    id: "bakery-problem",
    number: 3,
    data: {
      template: "content-visual",
      title: "The Bakery Problem",
      bullets: [
        { text: "You make croissants (x)\u2026", step: 1 },
        { text: "\u2026and muffins (y)", step: 2 },
        { text: "Croissants sell for $3, muffins for $4", step: 3 },
        { text: "Goal: maximize profit", bold: true, step: 4 },
        { text: "Maximize Profit = 3x + 4y", bold: true, step: 5 },
        { text: "Flour: 2x + 3y \u2264 100", color: "#ea580c", step: 6 },
        { text: "Sugar: x + 2y \u2264 50", color: "#2563eb", step: 7 },
        { text: "Labor: 3x + 2y \u2264 80", color: "#16a34a", step: 8 },
        { text: "x, y \u2265 0", step: 9 },
      ],
      visualId: "bakery-icon",
    },
  },
  {
    id: "defining-convexity",
    number: 4,
    data: {
      template: "content-visual",
      title: "Defining Convexity",
      bullets: [
        {
          text: "A set is convex if the line segment between any two points stays inside.",
          bold: true,
          step: 1,
        },
        { text: "Convex: filled disk. Not convex: crescent.", step: 2 },
        { text: "Why do we care?", bold: true, step: 3 },
        {
          text: "Every constraint defines a half-space \u2014 everything on one side of a line.",
          step: 4,
        },
        { text: "Half-spaces are convex.", step: 5 },
        { text: "Intersect convex sets \u2192 still convex.", step: 6 },
        {
          text: "The feasible region is always a convex polyhedron.",
          bold: true,
          step: 7,
        },
      ],
      visualId: "convexity-halfspace",
      visualStep: 1,
    },
  },
  {
    id: "standard-form",
    number: 5,
    data: {
      template: "math",
      title: "The Standard Algebraic Form",
      subtitle: "Every LP has the same structure \u2014 here it is, with our bakery mapped in.",
      rows: [
        {
          equation: "Maximize  z = c\u1d40x\u0304",
          annotation: "c = profit per unit, x\u0304 = (x, y) = (croissants, muffins). Bakery: c = (3, 4).",
          step: 1,
        },
        {
          equation: "Subject to  Ax\u0304 \u2264 b",
          annotation: "Each row of A is one constraint. Bakery: A = [[2,3],[1,2],[3,2]], b = (100, 50, 80) \u2014 flour, sugar, labor.",
          step: 2,
        },
        {
          equation: "x\u0304 \u2265 0",
          annotation: "Non-negativity \u2014 you can\u2019t make negative croissants.",
          step: 3,
        },
      ],
      footer: "That\u2019s the whole formulation. Three pieces: objective, constraints, non-negativity.",
    },
  },
  {
    id: "feasible-region",
    number: 6,
    data: {
      template: "full-visual",
      title: "Visualizing the Feasible Region",
      visualId: "feasible-region",
      caption:
        "Flour: 2x + 3y \u2264 100  \u00b7  Sugar: x + 2y \u2264 50  \u00b7  Labor: 3x + 2y \u2264 80  \u00b7  x, y \u2265 0",
      totalSteps: 1,
    },
  },
  {
    id: "vertices",
    number: 7,
    data: {
      template: "content-visual",
      title: "Vertices (Extreme Points)",
      bullets: [
        {
          text: "A vertex cannot be written as a convex combination of two other points in the set.",
          bold: true,
        },
        { text: "Intuition: the \u201ccorners\u201d \u2014 they stick out." },
      ],
      visualId: "vertices",
    },
  },
  {
    id: "fundamental-theorem",
    number: 8,
    data: {
      template: "theorem",
      label: "THEOREM",
      title: "The Fundamental Theorem of Linear Programming",
      statement:
        "If a linear program has an optimal solution, then it has an optimal solution at a vertex.",
      notes: [
        { text: "Condition 1: Feasible region is nonempty (constraints don\u2019t contradict).", step: 1 },
        { text: "Condition 2: Region is bounded in the optimization direction.", step: 2 },
        {
          text: "When both hold \u2014 the optimum exists, and it\u2019s at a corner.",
          bold: true,
          step: 3,
        },
        { text: "Infinitely many feasible points \u2192 only check finitely many vertices.", step: 4 },
        { text: "But why? Why can\u2019t the optimum hide in the middle?", step: 5 },
      ],
    },
  },
  {
    id: "level-set-sweep",
    number: 9,
    data: {
      template: "content-visual",
      title: "Why? The Level Set Argument",
      bullets: [
        { text: "Objective: Profit = 3x + 4y", step: 1 },
        { text: "Level sets = lines where profit is constant (e.g. 3x + 4y = 60)", step: 2 },
        { text: "As profit increases, the line sweeps in the gradient direction", step: 3 },
        { text: "Last contact with feasible region \u2192 vertex (15, 17.5), z* = $115", bold: true, step: 4 },
      ],
      visualId: "level-set",
    },
  },
  {
    id: "evaluating-vertices",
    number: 10,
    data: {
      template: "table",
      title: "Evaluating the Vertices",
      subtitle: "Objective: Profit = 3x + 4y",
      columns: ["Vertex (x, y)", "Binding Constraints", "Total Profit"],
      rows: [
        { cells: ["(0, 0)", "x = 0, y = 0", "$0"] },
        { cells: ["(0, 25)", "x = 0, Sugar", "$100"] },
        { cells: ["(26.67, 0)", "y = 0, Labor", "\u2248 $80"] },
        { cells: ["(15, 17.5)", "Sugar + Labor", "$115"], highlight: true },
      ],
      footer: "Flour has slack \u2014 it doesn\u2019t bind at the optimum.",
    },
  },
  {
    id: "beyond-two-dimensions",
    number: 11,
    data: {
      template: "content-visual",
      title: "Beyond Two Dimensions",
      bullets: [
        { text: "Our bakery: 2 variables, 4 vertices. Easy to draw.", step: 1 },
        { text: "Real problems: thousands of variables, millions of constraints.", step: 2 },
        { text: "But the geometry is the same. Convex polyhedron. Finite vertices. Optimum at a corner.", bold: true, step: 3 },
        { text: "The Simplex Method (Dantzig, 1947): start at a vertex, move to a better adjacent vertex, repeat.", step: 4 },
        { text: "The Fundamental Theorem is why this works \u2014 we know the answer is at some vertex.", step: 5 },
      ],
      visualId: "simplex-3d",
    },
  },
  {
    id: "lp-in-the-wild",
    number: 12,
    data: {
      template: "content-visual",
      title: "LP in the Wild",
      bullets: [
        {
          text: "Airlines: crew scheduling, gate assignment, ticket pricing \u2014 tens of thousands of variables daily.",
          color: "#0284c7",
          step: 1,
        },
        {
          text: "Logistics: Amazon routes 20M packages/day. Every truck, warehouse, driver \u2014 an LP.",
          color: "#ea580c",
          step: 2,
        },
        {
          text: "Power grids: which generators to run, renewable integration, load balancing \u2014 solved every few minutes.",
          color: "#16a34a",
          step: 3,
        },
        {
          text: "The theorem we proved today runs millions of times a day, across the global economy.",
          bold: true,
          step: 4,
        },
      ],
      visualId: "lp-wild",
    },
  },
  {
    id: "the-big-picture",
    number: 13,
    data: {
      template: "content-visual",
      title: "The Big Picture",
      bullets: [
        { text: "Linear constraints \u2192 convex polyhedron.", step: 1 },
        { text: "Convex polyhedra have finitely many vertices.", step: 2 },
        {
          text: "The optimum is always at a vertex. Infinite search \u2192 finite check.",
          bold: true,
          step: 3,
        },
        { text: "4 vertices in our bakery. Millions in an airline LP. Same theorem.", step: 4 },
        {
          text: "Deeper waters: duality, integer programming, approximation algorithms.",
          step: 5,
        },
      ],
      visualId: "big-picture",
    },
  },
];
