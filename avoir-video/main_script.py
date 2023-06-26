from manim import *
import numpy as np
import math


## The scene setup can be an annotation

def title_slide(s: Scene, section_name="title"):
    s.next_section(section_name)
    #img = ImageMobject("images/OSU-logo.png")
    img = SVGMobject("images/OSU-logo.svg")
    #img.scale(3)
    bg_rect = BackgroundRectangle(img, color=WHITE)
    title_text = r"\section*{Online Fairness Auditing \\ through Iterative Refinement}"
    text1 = Tex(title_text, height=1.5)
    text1.shift(UP)
    s.add(text1)
    text_emails = Tex(r'''\{maneriker.1, burley.22, parthasarathy.2\} \\
                      @osu.edu''')
    text_emails.shift(DOWN)
    s.add(text_emails)
    text_conf = Tex("KDD 2023")
    text_conf.shift(2*DOWN)
    s.add(text_conf)
    Group(img, bg_rect).next_to(text_conf, DOWN + LEFT)
    s.add(bg_rect)
    s.add(img)
    s.wait(duration=5*DEFAULT_WAIT_TIME)


def avoir_goal(s: Scene, section_name="avoir_goal"):
    #s.next_section(section_name, skip_animations=True)
    s.next_section(section_name)

    text2 = Tex(r'''\textbf{A}uditing and \textbf{V}erifying fairness \\ \textbf{O}nline through \textbf{I}terative \textbf{R}efinement''')
    text2.shift(2*UP)
    s.play(AddTextWordByWord(text2), run_time=4)
    text3 = Tex(r'''\textbf{AVOIR}''')
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

    seesaw_line = Line(start=2*LEFT, end=2*RIGHT)
    male_svg = SVGMobject("images/2/male.svg", height=0.8)
    female_svg = SVGMobject("images/2/female.svg", height=0.8)
    male_svg.next_to(seesaw_line.start, UP)
    female_svg.next_to(seesaw_line.end, UP)
    seesaw_except_base = Group(seesaw_line, male_svg, female_svg)
    tri_base = Triangle()
    tri_base.next_to(seesaw_line, DOWN)
    seesaw = Group(seesaw_except_base, tri_base)
    seesaw.next_to(svg_2, 5*DOWN)
    s.add(seesaw)
    
    # three part animation
    anim_seesaw = Succession(Rotate(seesaw_except_base, angle=PI/8, run_time=1.5),
                             Rotate(seesaw_except_base, angle=-PI/4, run_time=2),
                             lag_ratio=1)
    s.play(anim_seesaw, Create(func, run_time=4.5))

    s.wait()

def avoir_probabilstic_est(s: Scene, scene_name="avoir_challenge"):
    s.next_section(scene_name)
    tex_preamble = TexTemplate()
    tex_preamble.add_to_preamble('''
    \\usepackage{amsmath,amssymb}
    ''')
    head_text = Tex(r"\section*{AVOIR Probabilstic estimates}")
    head_text.shift(2* (UP))
    s.add(head_text)
    spec = MathTex(r'''
        \text{Specification } \psi
    ''', tex_template=tex_preamble)
    spec.shift(UP)
    s.play(Create(spec))
    s.wait()
    anytime_true = MathTex(r'P[', r'\forall t > 1', r', \psi] \geq 1-', r'\Delta', tex_template=tex_preamble)

    s.play(Create(anytime_true))
    s.wait()
    
    sel_rect_2 = SurroundingRectangle(anytime_true[3], color=BLUE)
    sel_text_2 = Tex("Threshold probability").scale(0.7)
    sel_text_2.next_to(sel_rect_2, DOWN)
    s.play(Create(sel_text_2), Create(sel_rect_2))
    s.play(FadeOut(sel_text_2, sel_rect_2))

    sel_rect_1 = SurroundingRectangle(anytime_true[1], color=YELLOW)
    sel_text_1 = Tex(r"\# Observed Samples").scale(0.7)
    sel_text_1.next_to(sel_rect_1, DOWN)
    text_describe_t = MathTex(r'\mathbf{\neq} \text{ Apriori sample size selection}')
    text_describe_t.next_to(sel_text_1, 2 * DOWN)
    s.play(Create(text_describe_t))
    s.play(Create(sel_rect_1))
    s.play(Create(sel_text_1))
    s.wait()
    s.play(FadeOut(sel_text_1, sel_rect_1))

    
def implementation(s: Scene, scene_name="implementaiton"):
    s.next_section(scene_name)
    chart_title = Tex(r"\section*{Implementation}")
    chart_title.shift(3*UP)
    s.add(chart_title)

    init_text_title = MathTex(r"\text{Decision Output } \implies")
    init_text_title.shift(2*UP)
    init_text = MathTex(r" \text{Random Variable } X \in \{0, 1\}")
    init_text.shift(UP)
    s.play(Create(init_text_title))
    s.play(Create(init_text))
    s.wait()

    formula_text = MathTex(r'P[|', r'\bar{E}_t[X] - E[X]| \geq \varepsilon(t, \delta)] \leq \delta', color=BLUE)
    #formula_text.shift()
    s.play(Create(formula_text))
    s.wait()
    movement_line = Line(start=formula_text.get_center(), end=2*UP)

    s.play(FadeOut(init_text), FadeOut(init_text_title))
    
    s.play(MoveAlongPath(formula_text, movement_line))    

    figure_ax = Axes(x_range=[0, 100, 20], y_range=[-0.2, 1.2, 0.5], y_length=3, x_length=8,
                     x_axis_config={
                        "longer_tick_multiple": 20
                     },
                     tips=False)
    figure_ax.next_to(formula_text, 2*DOWN)
    s.add(figure_ax)
    s.wait()

def optimization(s: Scene, scene_name="opt"):
    s.next_section(scene_name)
    title = Tex("\section*{Optimization and Auditing}")
    title.shift(2.5*UP)
    s.add(title)
    s.wait()

def thanks_slide(s: Scene, scene_name="thanks"):
    s.next_section(scene_name)
    title = Tex(r"\section*{Resources}")
    title.shift(2*UP)
    s.add(title)
    thanks_text = Tex("More details in the paper/code.").scale(0.7)
    
    s.play(Create(thanks_text))
    s.wait()

    code_link = Tex("https://github.com/pranavmaneriker/AVOIR", color=BLUE).scale(0.7)
    code_link.next_to(thanks_text, DOWN)

    s.play(FadeIn(code_link))
    s.wait()
    

class AVOIRVideo(Scene):
    def construct(self):
        # sections

        # slide 1:
        SLIDES = [3]
        #SLIDES = range(3)
        for s in SLIDES:
            self.make_slide(s)
            self.clear()

    def make_slide(self, sno):
        return {
            0: title_slide,
            1: avoir_goal,
            2: avoir_probabilstic_est,
            3: implementation,
            4: optimization,
            5: thanks_slide
        }[sno](self)