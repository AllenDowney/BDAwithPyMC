---
myst:
  html_meta:
    description: "A hands-on workshop on Bayesian A/B testing with PyMC: the beta-binomial model, Thompson sampling for adaptive experiments, and hierarchical models."
og:description: "A hands-on workshop on Bayesian A/B testing with PyMC: the beta-binomial model, Thompson sampling for adaptive experiments, and hierarchical models."
---

# Bayesian Decision Analysis with PyMC: Beyond A/B Testing

[Allen Downey](https://allendowney.com)

This hands-on workshop introduces practical Bayesian inference with PyMC, with a focus on A/B testing, decision-making under uncertainty, and hierarchical models. You'll learn how to build and interpret Bayesian models, compare alternatives with the probability of superiority instead of p-values, and use Thompson sampling to run adaptive experiments.

These methods are useful wherever people run experiments and make decisions with data: marketing, healthcare, public policy, product design, and general data science.

**Level:** intermediate. You should be comfortable with Python and NumPy, plotting, and Jupyter notebooks. You don't need any background in Bayesian statistics or PyMC.

**Length:** about 90 minutes.

## The notebook

[The workshop notebook](beta_binomial) is on this site with solutions. To do the exercises, run [the version with blanks on Colab](https://colab.research.google.com/github/AllenDowney/BDAwithPyMC/blob/main/notebooks/01_beta_binomial.ipynb). It has three parts:

1. **The beta-binomial model:** the conversion rate of an email campaign, the posterior distribution computed with PyMC, credible intervals, and why the prior matters when the dataset is small.
2. **Bayesian bandits:** an A/B test, the probability of superiority, and Thompson sampling.
3. **Hierarchical models:** sharing information between versions with hyperpriors, posterior predictive distributions, and a hierarchical model of batting averages in Major League Baseball.

## Recordings

I presented this workshop at [PyData Global 2025](https://www.youtube.com/watch?v=6yVIlWGNoGI), and it was the first session of the PyMC Labs course [Applied Bayesian Modeling](https://www.pymc-labs.com/courses/applied-bayesian-modeling). The code in the video is an earlier version; the [repository README](https://github.com/AllenDowney/BDAwithPyMC) lists the version that goes with it.

## Next steps

To go further, read [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

The code is on [GitHub](https://github.com/AllenDowney/BDAwithPyMC), under the MIT License; the text is under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
