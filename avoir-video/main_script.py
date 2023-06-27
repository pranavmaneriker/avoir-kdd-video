from manim import *
import numpy as np
import math
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService
#from manim_voiceover.services.coqui import CoquiService


## The scene setup can be an annotation

def title_slide(s: Scene, section_name="title"):
    s.next_section(section_name)
    #img = ImageMobject("images/OSU-logo.png")
    with s.voiceover(text="This circle is drawn as I speak.") as tracker:
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
    ####
    text_conf = Tex("KDD 2023")
    text_conf.shift(2*DOWN)
    s.add(text_conf)
    Group(img, bg_rect).scale(0.7).next_to(text1, UP +  LEFT)
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
    seesaw.next_to(svg_2, 4.5*DOWN)
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
    s.wait()
    s.play(Uncreate(sel_text_2, sel_rect_2))

    sel_rect_1 = SurroundingRectangle(anytime_true[1], color=YELLOW)
    sel_text_1 = Tex(r"\# Observed Samples").scale(0.7)
    sel_text_1.next_to(sel_rect_1, DOWN)
    text_describe_t = MathTex(r'\mathbf{\neq} \text{ Apriori sample size selection}')
    text_describe_t.next_to(sel_text_1, 2 * DOWN)
    s.play(Create(text_describe_t))
    s.play(Create(sel_rect_1))
    s.play(Create(sel_text_1))
    s.wait()
    s.play(Uncreate(sel_text_1, sel_rect_1))

    
def ah_confidence(t, delta):
    if t >= 5:
        return np.sqrt(0.6 * np.log(np.log(t)/np.log(1.1) + 5 * np.log(24/delta)/9))/np.sqrt(t)
    else:
        return 1e6

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

    formula_text = MathTex(r'P[|', r'\bar{E}_t[X]', r'- E[X]| \geq ', r'\varepsilon(t, \delta)',r'] \leq \delta', color=YELLOW)
    #formula_text.shift()
    s.play(Create(formula_text))
    s.wait()
    movement_line = Line(start=formula_text.get_center(), end=2*UP)

    s.play(FadeOut(init_text), FadeOut(init_text_title))
    
    s.play(MoveAlongPath(formula_text, movement_line))    

    x_min = 10
    x_max = 500
    total_time = 5
    coords_step = 100
    x_step = 50
    x_range = [x_min, x_max+20, x_step]
    y_range = [0, 2.5, 0.5]
    ax = Axes(x_range=x_range, y_range=y_range, y_length=3, x_length=8,
                     axis_config={'tip_shape': StealthTip})
    ax.next_to(formula_text, 3*DOWN)
    s.add(ax)
    delta = 0.1
    curve_col = BLUE_C
    bound_col = GREEN_B
    area_col = GRAY

    main_plot_func = lambda x:  0.5 + np.sin(x/coords_step)/(x/(coords_step+1))
    # plots
    curve = VGroup()
    lb_curve = VGroup()
    ub_curve = VGroup()
    areas = VGroup()
    
    # coordinates
    coords = [x_min, main_plot_func(20)]
    single_point = ax.c2p(*coords)
    ub_point = ax.c2p(coords[0], coords[1] + ah_confidence(x_min, delta))
    lb_point = ax.c2p(coords[0], coords[1] - ah_confidence(x_min, delta))
    curve_points = [single_point]
    ub_points = [ub_point]
    lb_points = [lb_point]

    curve.add(Line(single_point, single_point, color=curve_col))
    lb_curve.add(Line(ub_point, ub_point, color=bound_col))
    ub_curve.add(Line(lb_point, lb_point, color=bound_col))

    x_tracker = ValueTracker(x_min)
    rate = (x_max-x_min)/total_time

    def plot_updater(m, dt):
        m.set_value(m.get_value() + rate * dt)

    def redraw_curve():
        last_point = curve_points[-1]
        next_x = x_tracker.get_value()
        next_point = ax.c2p(next_x, main_plot_func(next_x))
        curve.add(Line(last_point, next_point, color=curve_col))
        curve_points.append(next_point)
        return curve

    def redraw_ub():
        last_point = ub_points[-1] 
        next_x = x_tracker.get_value()
        next_point = ax.c2p(next_x, main_plot_func(next_x) + ah_confidence(next_x, delta))
        ub_curve.add(Line(last_point, next_point, color=bound_col))
        ub_points.append(next_point)
        return ub_curve

    def redraw_lb():
        last_point = lb_points[-1] 
        next_x = x_tracker.get_value()
        next_point = ax.c2p(next_x, main_plot_func(next_x) - ah_confidence(next_x, delta))
        lb_curve.add(Line(last_point, next_point, color=bound_col))
        lb_points.append(next_point)
        return lb_curve
    
    def redraw_areas():
        ub_area = [ub_points[-1], ub_points[-2], curve_points[-2], curve_points[-1]]
        areas.add(Polygon(*ub_area, stroke_width=0).set_opacity(0.3).set_color(area_col))
        lb_area = [lb_points[-1], lb_points[-2], curve_points[-2], curve_points[-1]]
        areas.add(Polygon(*lb_area, stroke_width=0).set_opacity(0.3).set_color(area_col))
        return areas

    x_tracker.add_updater(plot_updater)
    redrawn_curve = always_redraw(redraw_curve)
    redrawn_ub = always_redraw(redraw_ub)
    redrawn_lb = always_redraw(redraw_lb)
    redrawn_areas = always_redraw(redraw_areas)


    s.add(x_tracker, redrawn_curve, redrawn_ub, redrawn_lb, redrawn_areas)
    
    #ub_plot = ax.plot(lambda x: main_plot_func(x) + ah_confidence(x, delta), color=RED)
    #bw_area = ax.get_area(ub_plot, [20, 1000], bounded_graph=main_plot, color=BLUE_B, fill_opacity=0.5)

    #all_plots = [Create(main_plot), Create(ub_plot), Write(bw_area)]
    #s.play(*all_plots)
    s.wait(total_time)
    x_tracker.remove_updater(plot_updater)
    sel_box = SurroundingRectangle(formula_text[1], color=curve_col)
    s.play(Create(sel_box))
    for _ in range(2):
        s.play(curve.animate.set_stroke(opacity=0))
        s.play(curve.animate.set_stroke(opacity=1))
    s.play(Uncreate(sel_box))
    sel_box = SurroundingRectangle(formula_text[3], color=area_col)
    s.play(Create(sel_box))
    for _ in range(2):
        s.play(areas.animate.set_fill(opacity=0))
        s.play(areas.animate.set_fill(opacity=1))
    
    s.play(areas.animate.set_fill(opacity=0.3), Uncreate(sel_box))

    s.wait()

def bern_sample(pr=0.5):
    return np.random.choice([0, 1], p=[1-pr, pr])

class StatefulSampler:
    def __init__(self, init_samples=0):
        self.n_samples = 0 
        self.sample_mean = 0
        for _ in range(init_samples):
            self.get_e()

    
    def get_e(self, *args):
        val = bern_sample()
        self.sample_mean = ((self.sample_mean * self.n_samples) + val)
        self.n_samples += 1
        self.sample_mean /= self.n_samples
        return self.sample_mean


def optimization(s: Scene, scene_name="opt"):
    s.next_section(scene_name)
    title = Tex("\section*{Optimization and Auditing}")
    title.shift(3*UP)
    x_range = [10, 100, 20]
    y_range = [0.2, 0.9, 0.2]
    step = 10
    COL_MAIN = BLUE_C
    COL_AREA = GRAY
    COL_B = GREEN_B
    def graph(seed=40):
        np.random.seed(seed)
        sampler = StatefulSampler(init_samples=x_range[0])
        left_axes = Axes(x_range, y_range, x_length=3, y_length=2)
        left_g = left_axes.plot(sampler.get_e, color=COL_MAIN)
        coords = left_axes.p2c([p for p in left_g.points])
        return left_axes, left_g, coords

    def plot_bounds(ub, lb, ax):
        b_areas = VGroup()
        for i in range(len(ub) - 1):
            b_areas.add(Polygon(ax.c2p(*ub[i]), ax.c2p(*ub[i+1]), ax.c2p(*lb[i+1]), ax.c2p(*lb[i]),
                                stroke_width=0).set_color(COL_AREA).set_opacity(0.5))
        return b_areas

    def gen_bounds(coords, curve, ax: Axes, delta=0.05, seed=40):
        bvals = [ah_confidence(c[0], delta) for c in coords]
        ub = [[c[0], c[1] + bval] for c, bval in zip(coords, bvals)]
        lb = [[c[0], c[1] - bval] for c, bval in zip(coords, bvals)]
        b_areas = plot_bounds(ub, lb, ax)
        return b_areas, ub, lb

    def combine_plot(lub, llb, lcoords, rub, rlb, rcoords, op="+"):
        if op == "+":
            c_lb = [[l[0], l[1] + r[1]] for l, r in zip(llb, rlb)]
            c_ub = [[l[0], l[1] + r[1]] for l, r in zip(lub, rub)]

            coords = [[l[0], l[1] + r[1]] for l, r in zip(lcoords, rcoords)]
        elif op == "*":
            # Does not work generally, but ok in this example
            c_lb = [[l[0], l[1] * r[1]] for l, r in zip(llb, rlb)]
            c_ub = [[l[0], l[1] * r[1]] for l, r in zip(lub, rub)]

            coords = [[l[0], l[1] * r[1]] for l, r in zip(lcoords, rcoords)]

        return c_lb, c_ub, coords




    s.add(title)
    s.wait()

    ### Plus animation
    def plus_animation():
        middle_op = MathTex(r"+").scale(2).set_color(YELLOW)
        middle_op.shift(UP)

        la, lg, lcoords = graph(seed=20)
        VGroup(la, lg).shift(3*LEFT + UP)
        larea_bounds, lub, llb = gen_bounds(lcoords, lg, la, 0.05)
        
        ra, rg, rcoords = graph(seed=40)
        VGroup(ra, rg).shift(3*RIGHT + UP)
        rarea_bounds, rub, rlb = gen_bounds(rcoords, rg, ra, 0.05)

        
        ba = Axes(x_range, [0, 2, 0.5], x_length=3, y_length=2)
        blb, bub, bcoords = combine_plot(lub, llb, lcoords, rub, rlb, rcoords, op="+")
        bg = [Line(ba.c2p(*pi), ba.c2p(*pii), color=COL_MAIN) for (pi, pii) in zip(bcoords, bcoords[1:])]
        bg = VGroup(*bg)
        VGroup(bg, ba).shift(2*DOWN)
        barea_bounds = plot_bounds(bub, blb, ba)


        s.play(Create(la), Create(ra), Create(ba))
        s.wait()
        s.play(Create(middle_op))
        s.wait()
        c_obs = [lg, larea_bounds, rg, rarea_bounds, bg, barea_bounds]
        s.play(*[Create(ob) for ob in c_obs])
        s.wait()
        s.play(*[Uncreate(ob) for ob in c_obs])
        s.wait()
        ### 
        return la, ra, ba, middle_op

    la, ra, ba, middle_op = plus_animation()

    def predefined_graph(ax, seed=42):
        np.random.seed(seed)
        sampler = StatefulSampler(init_samples=x_range[0])
        g = ax.plot(sampler.get_e, color=COL_MAIN)
        coords = ax.p2c([p for p in g.points])
        return ax, g, coords

    def mult_delta_animation(middle_op, la, ra, ba):
        new_middle = MathTex(r"\times").scale(2).set_color(YELLOW)
        new_middle.move_to(middle_op)
        s.play(Transform(middle_op, new_middle))

        _, lg, lcoords = predefined_graph(la, seed=20)
        _, rg, rcoords = predefined_graph(ra, seed=40)

        lareas, lub, llb = gen_bounds(lcoords, None, la, delta=1e10)
        rareas, rub, rlb = gen_bounds(rcoords, None, ra, delta=1e-9)

        bub, blb, bcoords = combine_plot(lub, llb, lcoords, rub, rlb, rcoords, op="*")
        bg = [Line(ba.c2p(*pi), ba.c2p(*pii), color=COL_MAIN) for (pi, pii) in zip(bcoords, bcoords[1:])]
        bg = VGroup(*bg)
        bareas = plot_bounds(bub, blb, ba)

        obs = [lg, rg, bg, lareas, rareas, bareas]
        s.play(*[Create(ob) for ob in obs])
        s.wait()
        import pdb
        #pdb.set_trace()

        def transform_deltas(delta_1=0.02, delta_2=0.08):
            lareas2, lub2, llb2 = gen_bounds(lcoords, None, la, delta=delta_1)
            rareas2, rub2, rlb2 = gen_bounds(rcoords, None, ra, delta=delta_2)
            #pdb.set_trace()

            bub2, blb2, bcoords2 = combine_plot(lub2, llb2, lcoords, rub2, rlb2, rcoords, op="*")
            bareas2 = plot_bounds(bub2, blb2, ba)
            return lareas2, rareas2, bareas2
        
        # hacky values for effect, IRL the t varies for each expression causing a bigger shift
        lareas2, rareas2, bareas2 = transform_deltas(1e-18, 1e10) 
        for _ in range(2):
            origs = [lareas.copy(), rareas.copy(), bareas.copy()]
            s.play(Transform(lareas, lareas2), Transform(rareas, rareas2), Transform(bareas, bareas2))
            #s.play(Create(lareas2), Create(rareas2), Create(bareas2), Uncreate(lareas), Uncreate(rareas), Uncreate(bareas))
            s.wait()
            s.play(Transform(lareas, origs[0]), Transform(rareas, origs[1]), Transform(bareas, origs[2]))
            s.wait()

        return la, lg, lareas, ra, rg, rareas, ba, bg, bareas


    la, lg, lareas, ra, rg, rareas, ba, bg, bareas = mult_delta_animation(middle_op, la, ra, ba)
    ## Move afuditing
    grp1 = VGroup(la, lg, lareas)
    grp1_copy = grp1.copy()
    grp2 = VGroup(ra, rg, rareas)
    grp2_copy = grp2.copy()
    grp3 = VGroup(ba, bg, bareas)
    s.play(Uncreate(grp1), Uncreate(grp2), Uncreate(middle_op))
    s.wait()

    s.play(grp3.animate.shift(3.5*UP))
    s.wait()
    lco = grp3.get_corner(LEFT + DOWN)
    rco = grp3.get_corner(RIGHT + DOWN)
    ar1 = Arrow(lco, lco + LEFT + DOWN)
    ar2 = Arrow(rco, rco + RIGHT + DOWN)
    s.play(Create(ar1), Create(ar2))
    grp1_copy.next_to(ar1, LEFT)
    grp2_copy.next_to(ar2, RIGHT)
    s.play(FadeIn(grp1_copy), FadeIn(grp2_copy))
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

    paper_link = Tex("https://doi.org/10.1145/3580305.3599454", color=GREEN).scale(0.7)
    paper_link.next_to(code_link, DOWN)

    tool_link = Tex(r"Video made using Manim (https://www.manim.community/)", color=YELLOW).scale(0.7)
    tool_link.next_to(paper_link, DOWN)

    s.play(Create(code_link))
    s.play(Create(paper_link))
    s.play(Create(tool_link))
    s.wait()

    
class AVOIRVideo(VoiceoverScene):
    def construct(self):
        # sections
        #self.set_speech_service(GTTSService())
        #self.set_speech_service(GTTSService())
        self.set_speech_service(RecorderService())

        # slide 1:
        #SLIDES = [3]
        SLIDES = range(6)
        #SLIDES = [4]
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
