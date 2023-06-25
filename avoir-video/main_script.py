from manim import *
import numpy as np
import math

def title_slide(s: Scene, section_name="title"):
    s.next_section(section_name)
    title_text = "\section*{Online Fairness Auditing \\\\ through Iterative Refinement}"
    text1 = Tex(title_text, height=1.5)
    text1.shift(UP)
    s.add(text1)
    text_emails = Tex('''\\{maneriker.1, burley.22, parthasarathy.2\\} \\\\
                      @osu.edu''')
    text_emails.shift(DOWN)
    s.add(text_emails)
    text_conf = Tex("KDD 2023")
    text_conf.shift(2*DOWN)
    s.add(text_conf)
    s.wait(duration=5*DEFAULT_WAIT_TIME)


def avoir_goal(s: Scene, section_name="avoir_goal"):
    s.next_section(section_name)

    text2 = Tex('''\\textbf{A}uditing and \\textbf{V}erifying fairness \\\\ \\textbf{O}nline through \\textbf{I}terative \\textbf{R}efinement''')
    text2.shift(2*UP)
    s.play(AddTextWordByWord(text2))
    text3 = Tex('''\\textbf{AVOIR}''')
    text3.shift(2*UP)
    s.play(Transform(text2, text3))

    svg_1 = SVGMobject("images/2/2_1.svg")
    svg_1.shift(3*LEFT)
    s.play(FadeIn(svg_1))

    svg_2 = SVGMobject("images/2/2_2.svg")
    arrow_1 = Arrow(start=2.25*LEFT, end=1.25 * LEFT)
    s.add(arrow_1)
    s.play(FadeIn(svg_2))

    arrow_2 = Arrow(start=1.25 * RIGHT, end=2.25 * RIGHT)
    s.add(arrow_2)

    axes = Axes(x_range=[0, 10], y_range=[0, 2.5], x_length = 1.5, y_length=1.5, tips=False)
    axes.shift(3 * RIGHT)
    s.play(FadeIn(axes))
    func = axes.plot(lambda x: 0.5 * np.sin(x) + 1, color=BLUE, x_range=[1, 9])

    seesaw_line = Line(start= DOWN, end=DOWN)
    seesaw_line.next_to(svg_2, DOWN)
    s.add(seesaw_line) 
    
    # three part animation
    s.play(Create(func))

    s.wait()



class AVOIRVideo(Scene):
    def construct(self):
        # sections

        # slide 1:
        #SLIDES = [0, 1]
        SLIDES = [1]
        for s in SLIDES:
            self.make_slide(s)
            self.clear()

        # slide 2

        #rect = Rectangle()
        #rect.set_fill(WHITE, opacity=1.0)
        #svg_img= SVGMobject("images/2/2_1.svg", opacity=1, height=2, width=2, color=WHITE)
        #self.add(rect)
        #self.add(svg_img)

        #self.wait()

    def make_slide(self, sno):
        return {
            0: title_slide,
            1: avoir_goal
        }[sno](self)


   # def construct_2(self):
   #     svg_img= SVGMobject("images/2/2_1.svg", opacity=0.5, height=2, width=2)
   #     circle = Circle(radius=1, color=BLUE)
   #     dot = Dot()
   #     dot2 = dot.copy().shift(RIGHT)
   #     self.add(dot)
   #     svg_img.next_to(circle)
   #     self.add(svg_img)

   #     line = Line([3, 0, 0], [5, 0, 0])
   #     self.add(line)

   #     self.play(Create(svg_img))
   #     self.play(GrowFromCenter(circle))
   #     self.play(Transform(dot, dot2))
   #     self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
   #     self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
   #     self.wait()