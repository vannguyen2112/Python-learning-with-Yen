from cProfile import label
from typing_extensions import runtime
from manim import *

def get_helper_function(color):
    result = VGroup()
    box = Rectangle(
        height=4, width=6, fill_color = color, fill_opacity=0.5, stroke_color=color
    )
    text = MathTex("ln(2").move_to(box.get_center())
    result.add(box, text)
    return result

class New(Scene):
    def construct(self):
        stuff = get_helper_function(color=BLUE)

        self.play(Create(stuff))
        self.play(stuff.animate.scale(1.5).to_edge(UL), run_time=3)
        self.play(stuff[0].animate.to_edge(RIGHT), run_time=2)

class ValueTrackers(Scene):
    def construct(self):
        k = ValueTracker(3.5)
        num =  always_redraw (lambda: 
        DecimalNumber().set_value(k.get_value()))
        

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0), run_time =3)

class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-4,4,1], x_length= 7, y_range=[0,16,4], y_length=8
        ).to_edge(DOWN).add_coordinates()

        labels= plane.get_axis_labels( x_label="x", y_label="f(x)")

        para = plane.plot(
            lambda x : x**2, x_range= [-4,4], color = GREEN
        )
        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels, para)))
        self.wait()
