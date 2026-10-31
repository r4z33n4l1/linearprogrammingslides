import numpy as np

from manim import *


BG = "#F7F0E1"
TEAL_FILL = "#14B8A6"
TEAL_STROKE = "#0F766E"
ORANGE_LINE = "#F97316"
BLUE_LINE = "#0284C7"
GREEN_LINE = "#16A34A"
RED_LINE = "#DC2626"
GOLD = "#EAB308"
GRAY_FILL = "#D6D3D1"


class LPScene(Scene):
    def setup(self):
        self.camera.background_color = BG

    def make_axes(
        self,
        x_range=(0, 5, 1),
        y_range=(0, 5, 1),
        x_length=6,
        y_length=6,
        x_label="x\u2081",
        y_label="x\u2082",
    ):
        axes = Axes(
            x_range=list(x_range),
            y_range=list(y_range),
            x_length=x_length,
            y_length=y_length,
            axis_config={"color": DARK_GRAY, "include_tip": False, "stroke_width": 3},
        )
        labels = axes.get_axis_labels(
            Text(x_label, color=DARK_GRAY, font_size=28),
            Text(y_label, color=DARK_GRAY, font_size=28),
        )
        return axes, labels

    def feasible_polygon(self, axes):
        vertices = [(0, 0), (0, 4), (1, 3), (2.5, 0)]
        polygon = Polygon(
            *[axes.c2p(x, y) for x, y in vertices],
            color=TEAL_STROKE,
            fill_color=TEAL_FILL,
            fill_opacity=0.35,
            stroke_width=4,
        )
        dots = VGroup(
            *[Dot(axes.c2p(x, y), color=TEAL_STROKE, radius=0.08) for x, y in vertices]
        )
        labels = VGroup(
            Text("(0,0)", font_size=20, color=BLACK).next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.14),
            Text("(0,4)", font_size=20, color=BLACK).next_to(axes.c2p(0, 4), LEFT, buff=0.14),
            Text("(1,3)", font_size=20, color=BLACK).next_to(axes.c2p(1, 3), UP + RIGHT, buff=0.14),
            Text("(5/2, 0)", font_size=20, color=BLACK).next_to(axes.c2p(2.5, 0), DOWN, buff=0.14),
        )
        return polygon, dots, labels

    def level_set_line(self, axes, alpha, x_max=5, y_max=5):
        points = []
        for x in (0, x_max):
            y = (alpha - 3 * x) / 2
            if 0 <= y <= y_max:
                points.append((x, y))
        for y in (0, y_max):
            x = (alpha - 2 * y) / 3
            if 0 <= x <= x_max:
                points.append((x, y))

        unique_points = []
        for point in points:
            if not any(
                abs(point[0] - existing[0]) < 1e-6
                and abs(point[1] - existing[1]) < 1e-6
                for existing in unique_points
            ):
                unique_points.append(point)

        if len(unique_points) < 2:
            return Line(axes.c2p(0, 0), axes.c2p(0, 0), stroke_opacity=0)

        unique_points.sort(key=lambda point: (point[0], point[1]))
        return DashedLine(
            axes.c2p(*unique_points[0]),
            axes.c2p(*unique_points[-1]),
            color=RED_LINE,
            dash_length=0.14,
            stroke_width=4,
        )


class ConvexityAnimation(LPScene):
    def construct(self):
        convex_shape = Circle(
            radius=1.6,
            color=DARK_GRAY,
            fill_color=GRAY_FILL,
            fill_opacity=0.9,
        )
        non_convex_shape = ArcPolygon(
            np.array([-1.5, 0.8, 0]),
            np.array([0.0, 1.55, 0]),
            np.array([1.5, 0.5, 0]),
            np.array([0.6, -1.15, 0]),
            np.array([-0.35, -0.45, 0]),
            np.array([-1.3, -1.25, 0]),
            color=DARK_GRAY,
            fill_color=GRAY_FILL,
            fill_opacity=0.9,
        )
        gap = Circle(radius=0.78, color=BG, fill_color=BG, fill_opacity=1).shift(0.55 * RIGHT)
        non_convex = VGroup(non_convex_shape, gap)

        left_group = VGroup(convex_shape)
        right_group = VGroup(non_convex)
        groups = VGroup(left_group, right_group).arrange(RIGHT, buff=2.6)

        left_a = Dot(convex_shape.point_at_angle(PI * 0.88), color=BLACK, radius=0.09)
        left_b = Dot(convex_shape.point_at_angle(-PI * 0.22), color=BLACK, radius=0.09)
        left_seg = Line(left_a.get_center(), left_b.get_center(), color=TEAL_STROKE, stroke_width=5)

        right_a = Dot(right_group.get_center() + LEFT * 0.9 + UP * 0.6, color=BLACK, radius=0.09)
        right_b = Dot(right_group.get_center() + RIGHT * 0.82 + UP * 0.48, color=BLACK, radius=0.09)
        right_seg = Line(right_a.get_center(), right_b.get_center(), color=RED_LINE, stroke_width=5)

        convex_label = Text("Convex", color=GREEN_LINE, font_size=30).next_to(left_group, DOWN, buff=0.3)
        non_convex_label = Text("Not Convex", color=RED_LINE, font_size=30).next_to(right_group, DOWN, buff=0.3)

        self.play(FadeIn(groups), run_time=0.8)
        self.play(FadeIn(left_a), FadeIn(left_b), Create(left_seg), run_time=0.9)
        self.play(FadeIn(right_a), FadeIn(right_b), Create(right_seg), run_time=0.9)
        self.play(Write(convex_label), Write(non_convex_label), run_time=0.7)
        self.wait(1.2)


class FeasibleRegionAnimation(LPScene):
    def construct(self):
        axes, labels = self.make_axes()
        graph = VGroup(axes, labels)

        line_one = axes.plot(lambda x: 4 - x, x_range=[0, 4], color=ORANGE_LINE, stroke_width=5)
        line_two = axes.plot(lambda x: 5 - 2 * x, x_range=[0, 2.5], color=BLUE_LINE, stroke_width=5)
        polygon, dots, dot_labels = self.feasible_polygon(axes)

        outside = Rectangle(
            width=6.4,
            height=6.2,
            fill_color="#FCA5A5",
            fill_opacity=0.16,
            stroke_opacity=0,
        ).move_to(axes)

        self.play(Create(axes), FadeIn(labels), run_time=1.0)
        self.play(FadeIn(outside), run_time=0.5)
        self.play(Create(line_one), run_time=0.8)
        self.play(Create(line_two), run_time=0.8)
        self.play(FadeOut(outside), FadeIn(polygon), run_time=0.8)
        self.play(FadeIn(dots), FadeIn(dot_labels), run_time=0.7)
        self.wait(1.0)


class LevelSetSweepAnimation(LPScene):
    """Level-set sweep for the bakery problem.

    Feasible vertices: (0,0), (80/3, 0), (15, 17.5), (0, 25)
    Objective: Profit = 3x + 4y
    Optimal vertex: (15, 17.5), z* = 115
    Level sets: 3x + 4y = c  =>  y = (c - 3x) / 4
    """

    XM = 50
    YM = 45

    def bakery_level_line(self, axes, c):
        """Return a DashedLine for 3x + 4y = c clipped to [0, XM] x [0, YM]."""
        pts = []
        # y-intercept: x=0 => y = c/4
        y0 = c / 4
        if 0 <= y0 <= self.YM:
            pts.append((0, y0))
        # x-intercept: y=0 => x = c/3
        x0 = c / 3
        if 0 <= x0 <= self.XM:
            pts.append((x0, 0))
        # top edge: y=YM => x = (c - 4*YM)/3
        xt = (c - 4 * self.YM) / 3
        if 0 < xt <= self.XM:
            pts.append((xt, self.YM))
        # right edge: x=XM => y = (c - 3*XM)/4
        yr = (c - 3 * self.XM) / 4
        if 0 < yr <= self.YM:
            pts.append((self.XM, yr))

        # deduplicate
        unique = []
        for p in pts:
            if not any(abs(p[0] - u[0]) < 0.01 and abs(p[1] - u[1]) < 0.01 for u in unique):
                unique.append(p)
        if len(unique) < 2:
            return Line(axes.c2p(0, 0), axes.c2p(0, 0), stroke_opacity=0)
        unique.sort()
        return DashedLine(
            axes.c2p(*unique[0]),
            axes.c2p(*unique[-1]),
            color=RED_LINE,
            dash_length=0.14,
            stroke_width=4,
        )

    def construct(self):
        axes, labels = self.make_axes(
            x_range=(0, self.XM, 10),
            y_range=(0, self.YM, 10),
            x_length=6.8,
            y_length=6.0,
            x_label="x",
            y_label="y",
        )

        # Bakery feasible polygon
        verts = [(0, 0), (80 / 3, 0), (15, 17.5), (0, 25)]
        polygon = Polygon(
            *[axes.c2p(x, y) for x, y in verts],
            color=TEAL_STROKE,
            fill_color=TEAL_FILL,
            fill_opacity=0.35,
            stroke_width=4,
        )
        dots = VGroup(*[Dot(axes.c2p(x, y), color=TEAL_STROKE, radius=0.07) for x, y in verts])

        # Gradient arrow in direction (3, 4) normalised, placed inside region
        grad_start = axes.c2p(5, 5)
        grad_end = axes.c2p(11, 13)
        direction = Arrow(
            start=grad_start,
            end=grad_end,
            buff=0,
            color=RED_LINE,
            stroke_width=6,
        )

        self.play(Create(axes), FadeIn(labels), run_time=1.2)
        self.play(FadeIn(polygon), FadeIn(dots), run_time=1.0)
        self.wait(0.4)

        # Sweep level sets from low to high
        alpha = ValueTracker(20)
        level = always_redraw(lambda: self.bakery_level_line(axes, alpha.get_value()))
        self.add(level)
        self.play(GrowArrow(direction), run_time=0.8)
        self.play(alpha.animate.set_value(60), run_time=1.4, rate_func=linear)
        self.play(alpha.animate.set_value(100), run_time=1.4, rate_func=linear)
        self.play(alpha.animate.set_value(115), run_time=1.2, rate_func=smooth)
        self.wait(0.3)

        # Highlight optimum at (15, 17.5), z* = 115
        optimal_dot = Dot(axes.c2p(15, 17.5), color=GOLD, radius=0.14)
        optimal_label = Text("z* = 115", color=BLACK, font_size=22).next_to(
            axes.c2p(15, 17.5), UP + RIGHT, buff=0.18
        )
        self.play(
            FadeIn(optimal_dot, scale=1.4),
            Flash(optimal_dot, color=GOLD),
            FadeIn(optimal_label),
            run_time=1.0,
        )
        self.wait(2.0)


class BakeryFeasibleRegion(LPScene):
    def construct(self):
        XM = 50  # axis max for x
        YM = 45  # axis max for y

        axes, labels = self.make_axes(
            x_range=(0, XM, 10),
            y_range=(0, YM, 10),
            x_length=6.8,
            y_length=6.0,
            x_label="x",
            y_label="y",
        )

        self.play(Create(axes), FadeIn(labels), run_time=1.4)
        self.wait(0.6)

        # Step 1: x, y >= 0  — shade the first quadrant
        quadrant = Polygon(
            axes.c2p(0, 0),
            axes.c2p(XM, 0),
            axes.c2p(XM, YM),
            axes.c2p(0, YM),
            fill_color=TEAL_FILL,
            fill_opacity=0.0,
            stroke_opacity=0,
        )
        self.play(quadrant.animate.set_fill(opacity=0.15), run_time=1.2)
        self.wait(0.8)

        # Step 2: Flour — 2x + 3y <= 100  =>  y = (100 - 2x)/3
        # Line from (0, 33.33) to (50, 0)
        flour_line = axes.plot(
            lambda x: (100 - 2 * x) / 3, x_range=[0, XM], color=ORANGE_LINE, stroke_width=5
        )
        # Feasible region after flour: quadrant ∩ flour
        # Vertices: (0,0), (50,0) clipped by flour at (50, 0), (0, 33.33)
        flour_region = Polygon(
            axes.c2p(0, 0),
            axes.c2p(XM, 0),
            axes.c2p(XM, 0),  # flour at x=50: y=0
            axes.c2p(0, 100 / 3),
            fill_color=TEAL_FILL,
            fill_opacity=0.0,
            stroke_opacity=0,
        )
        self.play(Create(flour_line), run_time=1.4)
        self.wait(0.3)
        self.play(
            FadeOut(quadrant),
            flour_region.animate.set_fill(opacity=0.18),
            run_time=1.2,
        )
        self.wait(0.8)

        # Step 3: Sugar — x + 2y <= 50  =>  y = (50 - x)/2
        # Line from (0, 25) to (50, 0)
        sugar_line = axes.plot(
            lambda x: (50 - x) / 2, x_range=[0, XM], color=BLUE_LINE, stroke_width=5
        )
        # Flour ∩ Sugar region.
        # Flour intercepts: (0, 33.33), (50, 0). Sugar intercepts: (0, 25), (50, 0).
        # Flour ∩ Sugar intersection: 2x+3y=100, x+2y=50 => x=50-2y => 2(50-2y)+3y=100 => 100-4y+3y=100 => y=0, x=50
        # So flour & sugar only meet at (50, 0). Sugar is tighter on y-axis (25 < 33.33).
        # Region: (0,0), (50,0), (0,25)
        sugar_region = Polygon(
            axes.c2p(0, 0),
            axes.c2p(XM, 0),
            axes.c2p(0, 25),
            fill_color=TEAL_FILL,
            fill_opacity=0.0,
            stroke_opacity=0,
        )
        self.play(Create(sugar_line), run_time=1.4)
        self.wait(0.3)
        self.play(
            FadeOut(flour_region),
            sugar_region.animate.set_fill(opacity=0.22),
            run_time=1.2,
        )
        self.wait(0.8)

        # Step 4: Labor — 3x + 2y <= 80  =>  y = (80 - 3x)/2
        # Line from (0, 40) to (26.67, 0)
        labor_line = axes.plot(
            lambda x: (80 - 3 * x) / 2, x_range=[0, 80 / 3], color=GREEN_LINE, stroke_width=5
        )
        # Final feasible region: (0,0), (80/3, 0), (15, 17.5), (0, 25)
        # Sugar ∩ Labor: x+2y=50, 3x+2y=80 => 2x=30 => x=15, y=17.5
        final_region = Polygon(
            axes.c2p(0, 0),
            axes.c2p(80 / 3, 0),
            axes.c2p(15, 17.5),
            axes.c2p(0, 25),
            fill_color=TEAL_FILL,
            fill_opacity=0.0,
            stroke_width=4,
            stroke_color=TEAL_STROKE,
            stroke_opacity=0,
        )
        self.play(Create(labor_line), run_time=1.4)
        self.wait(0.3)
        self.play(
            FadeOut(sugar_region),
            final_region.animate.set_fill(opacity=0.35).set_stroke(opacity=1),
            run_time=1.4,
        )
        self.wait(0.6)

        # Show vertices
        vertices = [(0, 0), (0, 25), (15, 17.5), (80 / 3, 0)]
        dots = VGroup(*[Dot(axes.c2p(x, y), color=TEAL_STROKE, radius=0.08) for x, y in vertices])
        point_labels = VGroup(
            Text("(0, 0)", font_size=18, color=BLACK).next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.12),
            Text("(0, 25)", font_size=18, color=BLACK).next_to(axes.c2p(0, 25), LEFT, buff=0.12),
            Text("(15, 17.5)", font_size=18, color=BLACK).next_to(axes.c2p(15, 17.5), UP + RIGHT, buff=0.12),
            Text("(26.67, 0)", font_size=18, color=BLACK).next_to(axes.c2p(80 / 3, 0), DOWN, buff=0.12),
        )
        self.play(FadeIn(dots), FadeIn(point_labels), run_time=1.2)
        self.wait(2.0)


class SimplexPathAnimation(LPScene):
    def construct(self):
        outer = Square(side_length=3.8, color=GRAY_B, stroke_width=3)
        inner = Square(side_length=2.5, color=GRAY_B, stroke_width=3).shift(
            RIGHT * 1.5 + UP * 1.1
        )
        connectors = VGroup(
            Line(outer.get_corner(DL), inner.get_corner(DL), color=GRAY_B),
            Line(outer.get_corner(DR), inner.get_corner(DR), color=GRAY_B),
            Line(outer.get_corner(UL), inner.get_corner(UL), color=GRAY_B),
            Line(outer.get_corner(UR), inner.get_corner(UR), color=GRAY_B),
        )
        tesseract = VGroup(outer, inner, connectors)

        path_points = [
            outer.get_corner(DL),
            outer.get_corner(DR),
            inner.get_corner(DR),
            inner.get_corner(UR),
            inner.get_corner(UL),
        ]
        path = VMobject(color=TEAL_STROKE, stroke_width=7)
        path.set_points_as_corners(path_points)
        endpoint = Dot(path_points[-1], color=GOLD, radius=0.14)

        self.play(Create(tesseract), run_time=1.2)
        self.play(Create(path), run_time=1.4)
        self.play(FadeIn(endpoint, scale=1.3), Flash(endpoint, color=GOLD), run_time=0.8)
        self.wait(1.0)


class SimplexWalk3D(ThreeDScene):
    """3D polytope with simplex edge-walk, camera slowly rotates."""

    def setup(self):
        self.camera.background_color = BG

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-40 * DEGREES)

        # Polytope: x+y+z<=4, x<=2.5, y<=2.5, z<=2.5, x,y,z>=0
        raw = np.array(
            [
                [0, 0, 0],  # 0
                [2.5, 0, 0],  # 1
                [0, 2.5, 0],  # 2
                [0, 0, 2.5],  # 3
                [2.5, 1.5, 0],  # 4
                [2.5, 0, 1.5],  # 5
                [1.5, 2.5, 0],  # 6
                [0, 2.5, 1.5],  # 7
                [1.5, 0, 2.5],  # 8
                [0, 1.5, 2.5],  # 9
            ]
        )
        center = raw.mean(axis=0)
        verts = raw - center

        edges_idx = [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 4),
            (1, 5),
            (2, 6),
            (2, 7),
            (3, 8),
            (3, 9),
            (4, 6),
            (5, 8),
            (7, 9),
            (4, 5),
            (6, 7),
            (8, 9),
        ]

        # Transparent faces for depth cue
        face_idx = [
            [0, 1, 4, 6, 2],  # z=0 face
            [0, 1, 5, 8, 3],  # y=0 face
            [0, 2, 7, 9, 3],  # x=0 face
            [4, 5, 8, 9, 7, 6],  # x+y+z=4 face
            [1, 4, 5],  # x=2.5 face
            [2, 6, 7],  # y=2.5 face
            [3, 8, 9],  # z=2.5 face
        ]
        faces = VGroup(
            *[
                Polygon(
                    *[verts[i] for i in f],
                    fill_color=TEAL_FILL,
                    fill_opacity=0.08,
                    stroke_opacity=0,
                )
                for f in face_idx
            ]
        )

        edge_lines = VGroup(
            *[
                Line3D(
                    verts[i],
                    verts[j],
                    color="#94a3b8",
                    thickness=0.02,
                )
                for i, j in edges_idx
            ]
        )

        dots = VGroup(
            *[Dot3D(v, color=TEAL_STROKE, radius=0.06) for v in verts]
        )

        # Simplex path: maximise x + 2y + 3z
        # (0,0,0)=0 → (0,0,2.5)=7.5 → (0,1.5,2.5)=10.5  (optimal)
        path_verts = [0, 3, 9]
        path_lines = [
            Line3D(
                verts[path_verts[i]],
                verts[path_verts[i + 1]],
                color=TEAL_STROKE,
                thickness=0.05,
            )
            for i in range(len(path_verts) - 1)
        ]

        moving_dot = Dot3D(verts[path_verts[0]], color=GOLD, radius=0.10)
        opt_dot = Dot3D(verts[path_verts[-1]], color=GOLD, radius=0.14)

        # Build scene
        self.play(Create(edge_lines), FadeIn(faces), FadeIn(dots), run_time=2.0)
        self.begin_ambient_camera_rotation(rate=0.10)
        self.wait(0.6)

        # Show moving dot at start
        self.play(FadeIn(moving_dot, scale=1.4), run_time=0.5)

        # Walk along simplex path
        for i, line in enumerate(path_lines):
            self.play(Create(line), run_time=1.0)
            self.play(
                moving_dot.animate.move_to(verts[path_verts[i + 1]]),
                run_time=0.6,
            )
            self.wait(0.3)

        # Highlight optimum
        self.play(
            Transform(moving_dot, opt_dot),
            run_time=0.6,
        )
        self.wait(3.5)
        self.stop_ambient_camera_rotation()


class DualityAnimation(LPScene):
    """Primal morphs into Dual: max→min, b→objective, c→RHS, A→Aᵀ."""

    def construct(self):
        # ── PRIMAL (separate pieces for animation) ──
        p_lbl = Text("Primal", font_size=30, color=TEAL_STROKE, weight=BOLD)

        p_max = Text("max", font_size=26, color=GOLD, weight=BOLD)
        p_obj = Text("3x + 4y", font_size=26, color=TEAL_STROKE)
        p_row0 = VGroup(p_max, p_obj).arrange(RIGHT, buff=0.18)

        p_c1_lhs = Text("2x + 3y", font_size=21, color=ORANGE_LINE)
        p_c1_ineq = Text("\u2264", font_size=21, color=BLACK)
        p_c1_rhs = Text("100", font_size=21, color=RED_LINE, weight=BOLD)
        p_c1 = VGroup(p_c1_lhs, p_c1_ineq, p_c1_rhs).arrange(RIGHT, buff=0.12)

        p_c2_lhs = Text("x + 2y", font_size=21, color=BLUE_LINE)
        p_c2_ineq = Text("\u2264", font_size=21, color=BLACK)
        p_c2_rhs = Text("50", font_size=21, color=RED_LINE, weight=BOLD)
        p_c2 = VGroup(p_c2_lhs, p_c2_ineq, p_c2_rhs).arrange(RIGHT, buff=0.12)

        p_c3_lhs = Text("3x + 2y", font_size=21, color=GREEN_LINE)
        p_c3_ineq = Text("\u2264", font_size=21, color=BLACK)
        p_c3_rhs = Text("80", font_size=21, color=RED_LINE, weight=BOLD)
        p_c3 = VGroup(p_c3_lhs, p_c3_ineq, p_c3_rhs).arrange(RIGHT, buff=0.12)

        p_nn = Text("x, y \u2265 0", font_size=21, color=DARK_GRAY)

        p_body = VGroup(p_row0, p_c1, p_c2, p_c3, p_nn).arrange(
            DOWN, buff=0.26, aligned_edge=LEFT
        )
        p_lbl.next_to(p_body, UP, buff=0.35)
        p_box = SurroundingRectangle(
            VGroup(p_lbl, p_body), color=TEAL_STROKE, buff=0.28,
            corner_radius=0.12, stroke_width=2.5,
        )
        primal = VGroup(p_box, p_lbl, p_body)

        # ── DUAL (target positions, revealed step by step) ──
        d_lbl = Text("Dual", font_size=30, color=RED_LINE, weight=BOLD)

        d_min = Text("min", font_size=26, color=GOLD, weight=BOLD)
        d_obj = Text("100\u03bb\u2081 + 50\u03bb\u2082 + 80\u03bb\u2083", font_size=22, color=RED_LINE)
        d_row0 = VGroup(d_min, d_obj).arrange(RIGHT, buff=0.18)

        d_dc1 = Text("2\u03bb\u2081 +  \u03bb\u2082 + 3\u03bb\u2083  \u2265  3", font_size=21, color=ORANGE_LINE)
        d_dc2 = Text("3\u03bb\u2081 + 2\u03bb\u2082 + 2\u03bb\u2083  \u2265  4", font_size=21, color=BLUE_LINE)
        d_nn = Text("\u03bb\u2081, \u03bb\u2082, \u03bb\u2083 \u2265 0", font_size=21, color=DARK_GRAY)

        d_body = VGroup(d_row0, d_dc1, d_dc2, d_nn).arrange(
            DOWN, buff=0.26, aligned_edge=LEFT
        )
        d_lbl.next_to(d_body, UP, buff=0.35)
        d_box = SurroundingRectangle(
            VGroup(d_lbl, d_body), color=RED_LINE, buff=0.28,
            corner_radius=0.12, stroke_width=2.5,
        )
        dual = VGroup(d_box, d_lbl, d_body)
        dual.shift(RIGHT * 3.3 + DOWN * 0.15)

        # Step labels helper
        def slabel(txt, clr=DARK_GRAY):
            return Text(txt, font_size=20, color=clr).to_edge(DOWN, buff=0.45)

        # Strong duality result
        strong = Text(
            "Strong Duality:  max z* = min w*  =  $115",
            font_size=24, color=TEAL_STROKE, weight=BOLD,
        ).to_edge(DOWN, buff=0.4)

        # ════════════════════════════════════════
        # ANIMATE
        # ════════════════════════════════════════

        # Phase 1: Show primal centered
        primal.move_to(ORIGIN + DOWN * 0.15)
        self.play(FadeIn(primal), run_time=1.8)
        self.wait(2.5)

        # Phase 2: Slide primal left
        self.play(primal.animate.shift(LEFT * 3.3), run_time=1.4)
        self.wait(0.8)

        # Dual label
        self.play(FadeIn(d_lbl), run_time=0.6)
        self.wait(0.4)

        # ── Step 1: max → min ──
        s1 = slabel("max  \u2192  min", GOLD)
        hl = SurroundingRectangle(p_max, color=GOLD, buff=0.06, stroke_width=3)
        self.play(Create(hl), FadeIn(s1), run_time=0.7)
        self.wait(0.8)

        max_ghost = p_max.copy()
        self.play(FadeTransform(max_ghost, d_min), run_time=1.4)
        self.play(FadeOut(hl), run_time=0.3)
        self.wait(0.8)

        # ── Step 2: b (RHS) becomes dual objective ──
        s2 = slabel("b = (100, 50, 80)  \u2192  dual objective", RED_LINE)
        hl1 = SurroundingRectangle(p_c1_rhs, color=RED_LINE, buff=0.06, stroke_width=3)
        hl2 = SurroundingRectangle(p_c2_rhs, color=RED_LINE, buff=0.06, stroke_width=3)
        hl3 = SurroundingRectangle(p_c3_rhs, color=RED_LINE, buff=0.06, stroke_width=3)
        self.play(
            FadeTransform(s1, s2),
            Create(hl1), Create(hl2), Create(hl3),
            run_time=0.8,
        )
        self.wait(1.0)

        rhs_ghosts = VGroup(p_c1_rhs.copy(), p_c2_rhs.copy(), p_c3_rhs.copy())
        self.play(FadeTransform(rhs_ghosts, d_obj), run_time=1.6)
        self.play(FadeOut(hl1), FadeOut(hl2), FadeOut(hl3), run_time=0.3)
        self.wait(0.8)

        # ── Step 3: A\u1d40 — transpose constraints, c becomes RHS ──
        s3 = slabel("A \u2192 A\u1d40,  c = (3, 4)  \u2192  dual RHS", ORANGE_LINE)
        hl_lhs = SurroundingRectangle(
            VGroup(p_c1_lhs, p_c2_lhs, p_c3_lhs), color=ORANGE_LINE,
            buff=0.08, stroke_width=3,
        )
        hl_obj = SurroundingRectangle(p_obj, color=TEAL_STROKE, buff=0.06, stroke_width=3)
        self.play(
            FadeTransform(s2, s3),
            Create(hl_lhs), Create(hl_obj),
            run_time=0.8,
        )
        self.wait(1.0)

        lhs_ghosts = VGroup(p_c1_lhs.copy(), p_c2_lhs.copy(), p_c3_lhs.copy())
        obj_ghost = p_obj.copy()
        self.play(
            FadeTransform(lhs_ghosts, d_dc1),
            run_time=1.6,
        )
        self.wait(0.4)
        self.play(
            FadeTransform(obj_ghost, d_dc2),
            run_time=1.6,
        )
        self.play(FadeOut(hl_lhs), FadeOut(hl_obj), run_time=0.3)
        self.wait(0.8)

        # ── Step 4: \u2264 flips to \u2265, non-negativity ──
        s4 = slabel("\u2264  \u2192  \u2265,  non-negativity carries over", DARK_GRAY)
        hl_ineqs = VGroup(
            SurroundingRectangle(p_c1_ineq, color=BLACK, buff=0.06, stroke_width=3),
            SurroundingRectangle(p_c2_ineq, color=BLACK, buff=0.06, stroke_width=3),
            SurroundingRectangle(p_c3_ineq, color=BLACK, buff=0.06, stroke_width=3),
        )
        self.play(FadeTransform(s3, s4), *[Create(h) for h in hl_ineqs], run_time=0.8)
        self.wait(0.8)

        nn_ghost = p_nn.copy()
        self.play(FadeTransform(nn_ghost, d_nn), run_time=1.2)
        self.play(*[FadeOut(h) for h in hl_ineqs], run_time=0.3)
        self.wait(0.6)

        # Dual box
        self.play(Create(d_box), run_time=0.6)
        self.wait(0.8)

        # ── Strong duality ──
        self.play(FadeTransform(s4, strong), run_time=1.0)
        self.wait(3.5)
