from manim import *

def get_enclosed_box(axes, x, color):
    p1 = Dot().move_to(axes.c2p(np.cos(x),np.sin(x))).set_color(PURPLE)
    p2 = Dot().move_to(axes.c2p(-np.cos(x),np.sin(x))).set_color(PURPLE)
    p3 = Dot().move_to(axes.c2p(-np.cos(x),-np.sin(x))).set_color(PURPLE)
    p4 = Dot().move_to(axes.c2p(np.cos(x),-np.sin(x))).set_color(PURPLE)

    area = Polygon(p1.get_center(), p2.get_center(), p3.get_center(), p4.get_center(),
    stroke_color = color, fill_color= color, fill_opacity = 0.5)

    result = VGroup(p1,p2,p3,p4, area)
    
    return result 



class Opti(Scene):
    def construct(self):
        axes = ( Axes(x_range=[-1.1,1.1], y_range=[-1.1,1.1], x_length =5, y_length =5)
        .to_edge(LEFT)
        .add_coordinates()
        
        )
        circle = axes.plot_parametric_curve(
            lambda t: [np.cos(t), np.sin(t)], t_range=[0,2*PI] 
            )

        k = ValueTracker(1*DEGREES) 

        area = always_redraw(
                lambda: get_enclosed_box( axes=axes, x = k.get_value(), color = BLUE)
                )
        plane = (
            Axes(x_range=[0,1.1], y_range=[0,2.1], x_length= 5, y_length=5)
            .to_edge(RIGHT)
            .add_coordinates()
        )
        
        graph = always_redraw(
            lambda: plane.plot(
                lambda x: 4 * x * (1 - x ** 2) ** 0.5,
                x_range = [0, np.sin(k.get_value())],
                color = YELLOW
            )
        )

        label = MathTex("f(x)= 4x\\sqrt{1-x^2}").next_to(plane, UP).set_color(YELLOW)

        self.add(axes, area, circle,plane,graph, label)
        self.play(k.animate.set_value(45 * DEGREES), run_time = 5, rate_functions = there_and_back_with_pause)
        self.wait()
        self.play(k.animate.set_value(85*DEGREES))
