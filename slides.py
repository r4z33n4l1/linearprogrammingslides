from manim import *
from manim_slides import Slide


class LPPresentation(Slide):
    AXIS_LIMIT = 5
    FEASIBLE_VERTICES = [(0, 0), (0, 4), (1, 3), (2.5, 0)]

    def clear_slide(self):
        if self.mobjects:
            fadeables = [mob for mob in self.mobjects if isinstance(mob, Mobject)]
            if fadeables:
                self.play(FadeOut(Group(*fadeables)), run_time=0.6)

    def build_axes(self):
        ax = Axes(
            x_range=[0, self.AXIS_LIMIT, 1],
            y_range=[0, self.AXIS_LIMIT, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": GREY_B, "include_tip": False},
        )
        labels = ax.get_axis_labels(MathTex("x_1"), MathTex("x_2"))
        return ax, labels

    def feasible_polygon(self, ax):
        return Polygon(
            *[ax.c2p(x, y) for x, y in self.FEASIBLE_VERTICES],
            color=TEAL,
            fill_color=TEAL,
            fill_opacity=0.3,
            stroke_width=3,
        )

    def vertex_dots(self, ax, color=YELLOW):
        return VGroup(
            *[
                Dot(ax.c2p(x, y), radius=0.075, color=color)
                for x, y in self.FEASIBLE_VERTICES
            ]
        )

    def vertex_labels(self, ax):
        labels = []
        offsets = {
            (0, 0): DOWN + LEFT,
            (0, 4): LEFT,
            (1, 3): UP + RIGHT,
            (2.5, 0): DOWN,
        }
        for point in self.FEASIBLE_VERTICES:
            point_text = r"\frac{5}{2}" if point[0] == 2.5 else str(point[0])
            label = MathTex(
                rf"\left({point_text},{point[1]}\right)"
            ).scale(0.55)
            label.next_to(ax.c2p(*point), offsets[point], buff=0.15)
            labels.append(label)
        return VGroup(*labels)

    def constraint_line(self, ax, equation, color):
        return ax.plot(equation, x_range=[0, self.AXIS_LIMIT], color=color)

    def level_set_segment(self, ax, alpha):
        points = []
        for x in (0, self.AXIS_LIMIT):
            y = (alpha - 3 * x) / 2
            if 0 <= y <= self.AXIS_LIMIT:
                points.append((x, y))
        for y in (0, self.AXIS_LIMIT):
            x = (alpha - 2 * y) / 3
            if 0 <= x <= self.AXIS_LIMIT:
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
            return Dot(ax.c2p(0, 0), radius=0.01, fill_opacity=0, stroke_opacity=0)

        unique_points.sort(key=lambda point: (point[0], point[1]))
        start, end = unique_points[0], unique_points[-1]
        return DashedLine(
            ax.c2p(*start),
            ax.c2p(*end),
            color=RED,
            dash_length=0.15,
        )

    def construct(self):
        tex_template = TexTemplate()
        tex_template.documentclass = r"\documentclass{article}"
        tex_template.tex_compiler = "pdflatex"
        tex_template.output_format = ".pdf"
        MathTex.set_default(tex_template=tex_template)
        Tex.set_default(tex_template=tex_template)

        # Slide 1: Title
        title = Text("What is Linear Programming?", font_size=48)
        subtitle = VGroup(
            Text("Razeen Ali", font_size=28),
            Text("MAT392", font_size=28, color=GREY_B),
        ).arrange(DOWN, buff=0.2)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(title, shift=UP), run_time=1.2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.0)
        self.next_slide()
        self.clear_slide()

        # Slide 2: Roadmap
        roadmap_title = Text("Roadmap", font_size=42).to_edge(UP)
        roadmap_items = VGroup(
            Text("1. Motivation and analogy", font_size=30),
            Text("2. Convexity", font_size=30),
            Text("3. LP definition", font_size=30),
            Text("4. Fundamental theorem", font_size=30),
            Text("5. Worked example", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        roadmap_items.next_to(roadmap_title, DOWN, buff=0.7).align_to(roadmap_title, LEFT)

        self.play(Write(roadmap_title))
        for item in roadmap_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.6)
        self.next_slide()
        self.clear_slide()

        # Slide 3: Factory analogy
        factory_title = Text("A Factory Analogy", font_size=42).to_edge(UP)
        product_boxes = VGroup(
            RoundedRectangle(width=2.0, height=1.2, corner_radius=0.15, color=BLUE),
            RoundedRectangle(width=2.0, height=1.2, corner_radius=0.15, color=GREEN),
        ).arrange(RIGHT, buff=1.2)
        product_labels = VGroup(
            Text("Product A", font_size=26).move_to(product_boxes[0]),
            Text("Product B", font_size=26).move_to(product_boxes[1]),
        )
        machine_placeholder = Circle(radius=0.7, color=GREY_B)
        machine_label = Text("Factory", font_size=24).move_to(machine_placeholder)
        machine_placeholder.move_to(ORIGIN + DOWN * 1.4)
        machine_label.move_to(machine_placeholder)
        product_boxes.move_to(UP * 0.5)
        product_labels[0].move_to(product_boxes[0])
        product_labels[1].move_to(product_boxes[1])
        arrows = VGroup(
            Arrow(machine_placeholder.get_top(), product_boxes[0].get_bottom(), buff=0.15),
            Arrow(machine_placeholder.get_top(), product_boxes[1].get_bottom(), buff=0.15),
        )
        factory_visual = VGroup(product_boxes, product_labels, machine_placeholder, machine_label, arrows)
        analogy_text = VGroup(
            Text("A factory makes two products.", font_size=28),
            Text("Time and raw materials are limited.", font_size=28),
            Text("We want the most profit possible.", font_size=28, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        analogy_text.next_to(factory_visual, DOWN, buff=0.7)

        self.play(Write(factory_title))
        self.play(FadeIn(product_boxes), FadeIn(product_labels), FadeIn(machine_placeholder), FadeIn(machine_label))
        self.play(GrowArrow(arrows[0]), GrowArrow(arrows[1]), run_time=1.0)
        for line in analogy_text:
            self.play(FadeIn(line, shift=RIGHT), run_time=0.6)
        self.next_slide()

        # Slide 4: LP solves this
        conclusion = Text("This is exactly what linear programming solves.", font_size=34, color=TEAL)
        conclusion.to_edge(DOWN)
        constraints = VGroup(
            Text("Decision variables", font_size=28),
            Text("Resource constraints", font_size=28),
            Text("Objective: maximize profit", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        constraints.next_to(factory_title, DOWN, buff=0.8).align_to(factory_title, LEFT)

        self.play(
            Transform(analogy_text, constraints),
            FadeIn(conclusion, shift=UP),
            run_time=1.0,
        )
        self.next_slide()
        self.clear_slide()

        # Slide 5: Convexity definition
        convex_title = Text("What Is Convexity?", font_size=42).to_edge(UP)
        convex_definition = MathTex(
            r"S \text{ is convex if } \lambda x + (1-\lambda)y \in S",
            r"\text{ for all } x,y \in S \text{ and } 0 \leq \lambda \leq 1."
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        convex_definition.next_to(convex_title, DOWN, buff=0.7)

        self.play(Write(convex_title))
        self.play(Write(convex_definition[0]), run_time=1.1)
        self.play(FadeIn(convex_definition[1], shift=UP), run_time=0.8)
        self.next_slide()

        # Slide 6: Convex vs non-convex
        convex_disk = Circle(radius=1.15, color=BLUE, fill_color=BLUE_E, fill_opacity=0.45)
        non_convex_ring = Annulus(
            inner_radius=0.45,
            outer_radius=1.15,
            color=ORANGE,
            fill_color=ORANGE,
            fill_opacity=0.4,
        )
        convex_group = VGroup(convex_disk, Text("Convex", font_size=28)).arrange(DOWN, buff=0.35)
        non_convex_group = VGroup(non_convex_ring, Text("Not Convex", font_size=28)).arrange(DOWN, buff=0.35)
        comparison = VGroup(convex_group, non_convex_group).arrange(RIGHT, buff=2.2)
        comparison.next_to(convex_definition, DOWN, buff=0.9)

        left_points = VGroup(
            Dot(convex_disk.point_at_angle(PI * 0.8), color=YELLOW),
            Dot(convex_disk.point_at_angle(-PI * 0.25), color=YELLOW),
        )
        left_segment = Line(left_points[0].get_center(), left_points[1].get_center(), color=YELLOW)

        right_points = VGroup(
            Dot(non_convex_ring.point_at_angle(PI * 0.88), color=RED),
            Dot(non_convex_ring.point_at_angle(-PI * 0.05), color=RED),
        )
        right_segment = Line(right_points[0].get_center(), right_points[1].get_center(), color=RED)

        self.play(FadeIn(comparison), run_time=0.8)
        self.play(Create(left_segment), FadeIn(left_points), Create(right_segment), FadeIn(right_points), run_time=1.3)
        self.next_slide()
        self.clear_slide()

        # Slide 7: LP definition
        lp_title = Text("Linear Programming", font_size=42).to_edge(UP)
        lp_form = MathTex(
            r"\max \quad c^T x",
            r"\text{subject to} \quad Ax \leq b"
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        lp_form.scale(1.1).next_to(lp_title, DOWN, buff=0.9)

        self.play(Write(lp_title))
        self.play(Write(lp_form), run_time=1.3)
        self.next_slide()

        # Slide 8: Explain each term
        explanation_items = VGroup(
            MathTex(r"x", r"=", r"\text{decision variables}"),
            MathTex(r"c^T x", r"=", r"\text{objective function}"),
            MathTex(r"Ax \leq b", r"=", r"\text{constraints}"),
            MathTex(r"P = \{x : Ax \leq b\}", r"=", r"\text{feasible region}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        explanation_items.next_to(lp_form, DOWN, buff=0.8).align_to(lp_form, LEFT)

        for item in explanation_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.7)
        self.next_slide()
        self.clear_slide()

        # Slide 9: Build feasible region from constraints
        feasible_title = Text("Building the Feasible Region", font_size=42).to_edge(UP)
        ax, axis_labels = self.build_axes()

        c1_line = self.constraint_line(ax, lambda x: 4 - x, BLUE)
        c2_line = self.constraint_line(ax, lambda x: 5 - 2 * x, ORANGE)

        x1_region = Polygon(
            ax.c2p(0, 0),
            ax.c2p(5, 0),
            ax.c2p(5, 5),
            ax.c2p(0, 5),
            fill_color=BLUE_E,
            fill_opacity=0.08,
            stroke_opacity=0,
        )
        x2_region = x1_region.copy().set_fill(color=GREEN_E, opacity=0.08)
        c1_region = Polygon(
            ax.c2p(0, 0),
            ax.c2p(0, 4),
            ax.c2p(4, 0),
            fill_color=BLUE,
            fill_opacity=0.16,
            stroke_opacity=0,
        )
        c2_region = Polygon(
            ax.c2p(0, 0),
            ax.c2p(0, 5),
            ax.c2p(2.5, 0),
            fill_color=ORANGE,
            fill_opacity=0.16,
            stroke_opacity=0,
        )

        steps = VGroup(
            Text("1. x1 >= 0", font_size=26, color=BLUE_E),
            Text("2. x2 >= 0", font_size=26, color=GREEN_E),
            Text("3. x1 + x2 <= 4", font_size=26, color=BLUE),
            Text("4. 2x1 + x2 <= 5", font_size=26, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        steps.to_edge(RIGHT, buff=1.0).shift(UP * 0.2)

        self.play(Write(feasible_title))
        self.play(Create(ax), FadeIn(axis_labels), run_time=1.0)
        self.play(FadeIn(x1_region), FadeIn(steps[0], shift=RIGHT), run_time=0.7)
        self.play(FadeIn(x2_region), FadeIn(steps[1], shift=RIGHT), run_time=0.7)
        self.play(Create(c1_line), FadeIn(c1_region), FadeIn(steps[2], shift=RIGHT), run_time=1.0)
        self.play(Create(c2_line), FadeIn(c2_region), FadeIn(steps[3], shift=RIGHT), run_time=1.0)
        self.next_slide()

        # Slide 10: Final polytope and vertices
        feasible_polytope = self.feasible_polygon(ax)
        vertices = self.vertex_dots(ax)
        vertex_labels = self.vertex_labels(ax)
        intersection_text = Text("Intersection of all constraints", font_size=28, color=TEAL)
        intersection_text.to_edge(DOWN)

        self.play(FadeIn(feasible_polytope), run_time=0.9)
        self.play(FadeIn(vertices), FadeIn(vertex_labels), run_time=0.9)
        self.play(Indicate(feasible_polytope, color=TEAL), FadeIn(intersection_text, shift=UP), run_time=1.0)
        self.next_slide()
        self.clear_slide()

        # Slide 11: Vertices / extreme points
        vertex_title = Text("Vertices / Extreme Points", font_size=42).to_edge(UP)
        ax, axis_labels = self.build_axes()
        polytope = self.feasible_polygon(ax)
        vertices = self.vertex_dots(ax)
        labels = self.vertex_labels(ax)
        vertex_definition = Tex(
            "A vertex cannot be written as a convex combination",
            "of two other points in the set.",
        ).arrange(DOWN, buff=0.15)
        vertex_definition.next_to(vertex_title, DOWN, buff=0.6)

        self.play(Write(vertex_title))
        self.play(FadeIn(vertex_definition, shift=UP), run_time=0.9)
        self.play(Create(ax), FadeIn(axis_labels), FadeIn(polytope), FadeIn(vertices), FadeIn(labels), run_time=1.0)
        self.play(LaggedStart(*[Flash(dot, color=YELLOW) for dot in vertices], lag_ratio=0.15), run_time=1.4)
        self.next_slide()
        self.clear_slide()

        # Slide 12: Fundamental theorem statement
        theorem_title = Text("Fundamental Theorem", font_size=42).to_edge(UP)
        theorem_statement = Tex(
            "If an LP has an optimal solution,",
            "then it has an optimal solution at a vertex.",
        ).arrange(DOWN, buff=0.25)
        theorem_statement.next_to(theorem_title, DOWN, buff=0.9)
        example_lp = MathTex(
            r"\max \; 3x_1 + 2x_2",
            r"\quad \text{s.t. } x_1 + x_2 \leq 4,\; 2x_1 + x_2 \leq 5,\; x_1,x_2 \geq 0"
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        example_lp.scale(0.9).next_to(theorem_statement, DOWN, buff=0.8)

        self.play(Write(theorem_title))
        self.play(FadeIn(theorem_statement, shift=UP), run_time=1.0)
        self.play(Write(example_lp), run_time=1.1)
        self.next_slide()

        # Slide 13: Level set sweep
        ax, axis_labels = self.build_axes()
        polytope = self.feasible_polygon(ax)
        vertices = self.vertex_dots(ax, color=WHITE)
        optimal_vertex = Dot(ax.c2p(1, 3), radius=0.095, color=YELLOW)
        optimal_label = MathTex(r"(1,3)").scale(0.6).next_to(optimal_vertex, UR, buff=0.12)
        objective_label = MathTex(r"c = (3,2)").to_corner(UR)

        alpha_tracker = ValueTracker(0)
        level_line = always_redraw(lambda: self.level_set_segment(ax, alpha_tracker.get_value()))
        alpha_text = always_redraw(
            lambda: VGroup(
                MathTex(r"\alpha ="),
                DecimalNumber(alpha_tracker.get_value(), num_decimal_places=1),
            )
            .arrange(RIGHT, buff=0.15)
            .to_corner(UL)
        )

        theorem_caption = Text("Push the level set in the direction of c", font_size=28, color=RED)
        theorem_caption.to_edge(DOWN)

        self.play(
            FadeOut(theorem_statement),
            FadeOut(example_lp),
            Create(ax),
            FadeIn(axis_labels),
            FadeIn(polytope),
            FadeIn(vertices),
            FadeIn(objective_label),
            run_time=1.0,
        )
        self.add(level_line, alpha_text)
        self.play(FadeIn(theorem_caption, shift=UP), run_time=0.6)
        self.play(alpha_tracker.animate.set_value(3), run_time=1.0, rate_func=linear)
        self.play(alpha_tracker.animate.set_value(6), run_time=1.0, rate_func=linear)
        self.play(alpha_tracker.animate.set_value(9), run_time=2.2, rate_func=linear)
        self.play(FadeIn(optimal_vertex), FadeIn(optimal_label), Flash(optimal_vertex, color=YELLOW), run_time=1.1)
        optimal_value = Text("Optimal value = 9 at (1, 3)", font_size=28, color=YELLOW)
        optimal_value.next_to(theorem_caption, UP, buff=0.25)
        self.play(FadeIn(optimal_value, shift=UP), run_time=0.7)
        self.next_slide()
        self.clear_slide()

        # Slide 14: Worked example summary
        summary_title = Text("Worked Example Summary", font_size=42).to_edge(UP)
        summary_lp = MathTex(
            r"\max \; 3x_1 + 2x_2",
            r"x_1 + x_2 \leq 4",
            r"2x_1 + x_2 \leq 5",
            r"x_1, x_2 \geq 0",
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        summary_lp.scale(0.95).next_to(summary_title, DOWN, buff=0.6).to_edge(LEFT, buff=0.9)

        header = VGroup(
            Tex("Vertex", font_size=30),
            MathTex(r"z = 3x_1 + 2x_2"),
        ).arrange(RIGHT, buff=1.3)
        rows = VGroup(
            VGroup(MathTex(r"(0,0)"), MathTex(r"0")).arrange(RIGHT, buff=2.2),
            VGroup(MathTex(r"(0,4)"), MathTex(r"8")).arrange(RIGHT, buff=2.2),
            VGroup(MathTex(r"(1,3)"), MathTex(r"9")).arrange(RIGHT, buff=2.2),
            VGroup(MathTex(r"\left(\frac{5}{2},0\right)"), MathTex(r"7.5")).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        table = VGroup(header, Line(LEFT * 2.2, RIGHT * 2.2), rows).arrange(
            DOWN, aligned_edge=LEFT, buff=0.25
        )
        table.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.2)
        optimal_row_box = SurroundingRectangle(rows[2], color=YELLOW, buff=0.12)
        optimal_marker = Text("optimal", font_size=24, color=YELLOW)
        optimal_marker.next_to(optimal_row_box, RIGHT, buff=0.2)

        self.play(Write(summary_title))
        self.play(Write(summary_lp), run_time=1.1)
        self.play(FadeIn(table, shift=LEFT), run_time=1.0)
        self.play(Create(optimal_row_box), FadeIn(optimal_marker, shift=RIGHT), run_time=0.8)
        self.next_slide()
        self.clear_slide()

        # Slide 15: Historical context and significance
        history_title = Text("Historical Context and Significance", font_size=38).to_edge(UP)
        history_points = VGroup(
            Text("George Dantzig introduced the simplex method in 1947.", font_size=28),
            Text("LP turns an infinite search into a finite vertex check.", font_size=28),
            Text("Applications include diet, logistics, scheduling, and finance.", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        history_points.next_to(history_title, DOWN, buff=0.8).to_edge(LEFT, buff=0.9)
        closing = Text("Linear programming makes optimization geometric and computable.", font_size=30, color=TEAL)
        closing.to_edge(DOWN, buff=1.0)

        self.play(Write(history_title))
        for point in history_points:
            self.play(FadeIn(point, shift=RIGHT), run_time=0.7)
        self.play(FadeIn(closing, shift=UP), run_time=0.8)
        self.next_slide()
        self.clear_slide()

        # Slide 16: Questions
        questions = Text("Questions?", font_size=54)
        recap = VGroup(
            Text("Convex feasible regions", font_size=28),
            Text("Vertices matter", font_size=28),
            Text("Optimal solutions occur at corners", font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.25)
        recap.next_to(questions, DOWN, buff=0.8)
        contact = Text("MAT392 | Linear Programming", font_size=24, color=GREY_B)
        contact.to_edge(DOWN)

        self.play(FadeIn(questions, scale=0.9), run_time=1.0)
        self.play(FadeIn(recap, shift=UP), run_time=0.9)
        self.play(FadeIn(contact), run_time=0.6)
        self.next_slide()
