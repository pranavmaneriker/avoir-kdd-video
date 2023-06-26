AVOIR Promotional Video
===============

## Description

> Instructions: You are expected to provide a very short description of your promotional video and is limited to 1,024 characters (which includes spaces) and be an actual description of the video (something original), not the abstract of your submission.
If your description text exceeds 1,024 characters, the description will be removed and "Promotional Video" used..
NOTE: Authors cannot upload their videos to their own, corporate, or institution's YouTube Channels.

A sizable proportion of deployed machine learning models make their decisions in a black-box manner.
Such decision-making procedures are susceptible to intrinsic biases, which has led to a call for accountability in deployed decision systems. 
In this video, we describe the main ideas behind AVOIR.
AVOIR is an automated, probabilistic inference-based system for tracking the runtime fairness properties of black-box machine learning decision systems. 

AVOIR provably improves upon guarantees provided by prior work and also provides a visual mechanism to audit models that violate fairness properties. AVOIR is applicable across a wide range of group fairness definitions. 

***
***
# Slides

In the remainder,
```
Describes accompanying animations
```

> Is the spoken text accompanying the slide

## 1. Online Fairness Auditing through Iterative Refinement

### Runtime audting of Machine Learning Models

**A**uditing and **V**erifying fairness **O**nline through **I**terative **R**efinement 
 <-> AVOIR

Pranav Maneriker, Codi Burley, Srinivasan Parthasarathy

{maneriker.1, burley.22, parthasarathy.2}@osu.edu


*** 
## 2. Goal

> We want to build an auditing tool to estimate the fairness of arbitrary, black box machine learning model at runtime, that is, online, as the data streams in.

![img1](images/2/2_1.svg) -> ![img1](images/2/2_2.svg) -> ![img2](images/2/2_3.svg)

```
Animate here
Seesaw with male and female
```



*** 
## 3. Challenge
> The runtime behavior of a model may differ from what that at training time and thus, that is when we want to make estimates of its fairness behavior.

> AVOIR needs to make probabilistic assertions, which look like
```
Assertion here
```
> This can be challenging

> we cannot apriori decide the sample size m, because we may be forced to discard collected data. Peeking at values would be equivalent to p-hacking.


*** 
## 4. Implementation

> We start with confidence sets that can make probabilistic guarantees in the online setting of the form 
```
Confidence statement expression and plot
```

> and these guarantees are asymptotically true. We call these terms elementary subexpressions


> We then devise a grammar and inference rules that allow computation of guarantees are combinations of these elementary subepressions.

```
Show graph combination of two terms producing an overall confidence
```
***
## 5. Challenge: Optimization
> The next question is this - given a fixed budget/probability threshold, can we distribute it such that we can achieve this across multiple expressions while minimizing the total number of samples?

```
Animation for these samples
```

> We develop optimizaiton inference rules within AVOIR which can provably achieve guarantees in fewer steps than prior state-of-the art.


***
### 6. Thanks, references, credits.

> Please see our paper and talk for further details and case studies showing how AVOIR can be used with real world data! 
```
Show example graphs from case studies
```
Paper link: https://doi.org/10.1145/3580305.3599454
Code link: https://github.com/pranavmaneriker/AVOIR





