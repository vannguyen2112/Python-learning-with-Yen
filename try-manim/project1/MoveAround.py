from manim import *

class Box(Scene):
    def construct(self):
        
        box = Rectangle(stroke_color = GREEN, stroke_opacity = 0.7,
        fill_color = RED, fill_opacity=0.5, height=1, width =1)

        self. add(box)
        self.play(box.animate.shift(RIGHT*2), run_time =2)
        self.play(box.animate.shift(UP*3), run_time=2)
        self.play(box.animate.shift(DOWN*5 + LEFT*5), run_time=2)
        self.play(box.animate.shift(UP*1.5 + RIGHT*1), run_time=2)

class FittingObjects(Scene):
    def construct(self):
        
        axes = Axes(
            x_range = [-3,3,1],
            y_range =[-3,3,1],
            x_length =6,
            y_length =6 
            )
        axes.to_edge(LEFT, buff=0.5)

        circle = Circle(stroke_width =6, stroke_color = YELLOW,
        fill_color= RED, fill_opacity = 0.8)
        circle.set_width(2).to_edge(DR,buff=0)

        triangle = Triangle(stroke_color = ORANGE, stroke_width = 10,
        fill_color = GREY).set_height(2).shift(DOWN*3 + RIGHT *3)

        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(Transform(circle,triangle), run_time = 3)