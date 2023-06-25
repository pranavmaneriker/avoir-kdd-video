Script for Talk
===============

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

> AVOIR makes probabilistic assertions, which look like
```
Assertion here
```
> This comes with a few challenges.

> First, we cannot apriori decide the sample size m, because we may be forced to discard collected data.






