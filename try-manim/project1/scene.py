from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class FirstExample(Scene):
	def construct(self):
		blue_circle = Circle(color= BLUE, fill_opacity=0.5)
		green_square = Square(color=GREEN, fill_opacity =0.8)
		green_square.next_to(blue_circle, RIGHT)
		self.add(blue_circle,green_square)

class SecondExample(Scene):
	def construct(self):
		ax= Axes(x_range=(-3,3),y_range=(-3,3))
		curve =ax.plot(lambda x: (x+2)*x*(x-2)/2, color=RED)
		area = ax.get_area(curve, x_range=(-2,0))
		self.play(Create(ax), run_time=3)
		self.play(Create(curve))
		self.play(FadeIn(area))
		self.wait(2)
		#self.add(ax,curve,area)

class SquareToCircle(Scene):
	def construct(self):
		green_square = Square(color= GREEN,fill_opacity= 0.8)
		self.play(DrawBorderThenFill(green_square))
		blue_circle = Circle(color=BLUE, fill_opacity=0.5)
		self.play(ReplacementTransform(green_square, blue_circle))
		self.play(Indicate(blue_circle))
		self.play(FadeOut(blue_circle))

class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        self.add(ax, graph)