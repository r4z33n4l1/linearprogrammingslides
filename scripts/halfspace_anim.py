from manim import *


class HalfSpaceAnimation(Scene):
    def construct(self):
        self.camera.background_color = "#f7f0e1"

        ax = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "color": "#94a3b8",
                "include_tip": True,
                "tip_length": 0.2,
                "stroke_width": 2,
            },
        )

        self.play(Create(ax, run_time=0.8))
        self.wait(0.3)

        # Constraint line: x + y = 3  =>  y = 3 - x
        # Visible from (0,3) to (3,0) within our range, extend a bit
        line = ax.plot(
            lambda x: 3 - x,
            x_range=[-0.5, 4.5],
            color="#334155",
            stroke_width=3,
        )

        self.play(Create(line, run_time=1.2))
        self.wait(0.4)

        # Half-space BELOW the line: x + y <= 3
        # Polygon covering the area below line within viewport
        below_poly = Polygon(
            ax.c2p(-1, -1),      # bottom-left corner
            ax.c2p(5, -1),       # bottom-right corner
            ax.c2p(5, 3 - 5),    # (5, -2) — line at x=5, clipped to bottom
            ax.c2p(4.5, 3 - 4.5),  # on the line
            ax.c2p(-0.5, 3 - (-0.5)),  # on the line
            ax.c2p(-1, 3 - (-1)),  # (−1, 4) — line at x=-1
            fill_color=BLUE,
            fill_opacity=0.0,
            stroke_opacity=0,
        )
        # Simpler: just use the corners that bound the below region
        below_poly = Polygon(
            ax.c2p(-1, -1),
            ax.c2p(5, -1),
            ax.c2p(5, -2),       # below line at x=5
            ax.c2p(-1, 4),       # line at x=-1: y=4
            fill_color="#3b82f6",
            fill_opacity=0.0,
            stroke_opacity=0,
        )

        self.play(below_poly.animate.set_fill(opacity=0.22), run_time=1.0)
        self.wait(0.6)

        # Half-space ABOVE the line: x + y >= 3
        above_poly = Polygon(
            ax.c2p(-1, 4),       # line at x=-1: y=4
            ax.c2p(5, -2),       # line at x=5: y=-2
            ax.c2p(5, 5),        # top-right
            ax.c2p(-1, 5),       # top-left
            fill_color="#f97316",
            fill_opacity=0.0,
            stroke_opacity=0,
        )

        self.play(above_poly.animate.set_fill(opacity=0.22), run_time=1.0)
        self.wait(0.8)

        # Fade out above, keep below
        self.play(FadeOut(above_poly), run_time=0.5)

        # Second constraint: 2x - y = 2  =>  y = 2x - 2
        # At x=0: y=-2, at x=3: y=4
        line2 = ax.plot(
            lambda x: 2 * x - 2,
            x_range=[0.5, 3.5],
            color="#16a34a",
            stroke_width=3,
        )

        # Below line2: 2x - y <= 2  =>  y >= 2x - 2  =>  ABOVE the line
        above_line2 = Polygon(
            ax.c2p(-1, 2 * (-1) - 2),  # (-1, -4)
            ax.c2p(3.5, 2 * 3.5 - 2),  # (3.5, 5)
            ax.c2p(-1, 5),
            fill_color="#16a34a",
            fill_opacity=0.0,
            stroke_opacity=0,
        )

        self.play(Create(line2, run_time=1.0))
        self.play(above_line2.animate.set_fill(opacity=0.18), run_time=0.8)
        self.wait(0.3)

        # Show intersection: x + y <= 3 AND y >= 2x - 2
        # Intersection of lines: x + y = 3 and y = 2x - 2
        # x + (2x - 2) = 3 => 3x = 5 => x = 5/3 ≈ 1.67, y = 2(5/3) - 2 = 4/3 ≈ 1.33
        ix, iy = 5 / 3, 4 / 3

        # Intersection region vertices (feasible):
        # - Where x+y=3 meets y-axis: (0, 3)
        # - Where the two lines meet: (5/3, 4/3)
        # - Where y=2x-2 meets x-axis: (1, 0)
        # - Origin area: (0, 0) is feasible (0+0<=3 and 0>=−2 ✓)
        # Actually let's just use: bounded by x+y<=3 above and y>=2x-2 below,
        # plus the viewport
        intersection_poly = Polygon(
            ax.c2p(0, 3),        # x+y=3 on y-axis
            ax.c2p(ix, iy),      # intersection point
            ax.c2p(1, 0),        # y=2x-2 on x-axis
            ax.c2p(0, 0),        # origin
            fill_color="#0d9488",
            fill_opacity=0.0,
            stroke_width=2,
            stroke_color="#0d9488",
            stroke_opacity=0.0,
        )

        self.play(
            FadeOut(below_poly),
            FadeOut(above_line2),
            intersection_poly.animate.set_fill(opacity=0.35).set_stroke(opacity=0.8),
            run_time=1.2,
        )

        # Flash the intersection vertex
        vertex_dot = Dot(ax.c2p(ix, iy), radius=0.1, color="#eab308")
        origin_dot = Dot(ax.c2p(0, 0), radius=0.08, color="#eab308")
        y_int_dot = Dot(ax.c2p(0, 3), radius=0.08, color="#eab308")
        x_int_dot = Dot(ax.c2p(1, 0), radius=0.08, color="#eab308")

        self.play(
            FadeIn(vertex_dot),
            FadeIn(origin_dot),
            FadeIn(y_int_dot),
            FadeIn(x_int_dot),
            Flash(vertex_dot, color="#eab308"),
            run_time=0.8,
        )
        self.wait(1.5)
