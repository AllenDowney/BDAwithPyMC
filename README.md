# Bayesian Decision Analysis with PyMC

[![tests](https://github.com/AllenDowney/BDAwithPyMC/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/BDAwithPyMC/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com)

**Beyond A/B Testing.** This hands-on workshop introduces practical Bayesian inference with PyMC, with a focus on A/B testing, decision-making under uncertainty, and hierarchical models. You'll learn how to build and interpret Bayesian models, compare alternatives with the probability of superiority instead of p-values, and use Thompson sampling to run adaptive experiments.

These methods are useful wherever people run experiments and make decisions with data: marketing, healthcare, public policy, product design, and general data science.

This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops).

**Level:** intermediate. You should be comfortable with Python and NumPy, plotting, and Jupyter notebooks. You don't need any background in Bayesian statistics or PyMC.

**Length:** about 90 minutes.

## Outline

1. **The beta-binomial model:** the conversion rate of an email campaign. A beta prior, a binomial likelihood, and a posterior distribution computed with PyMC; credible intervals; and why the prior matters when the dataset is small (a rookie who gets 3 hits in 3 at bats).
2. **Bayesian bandits:** an A/B test of two versions of the email. The distribution of the difference, the probability of superiority, and Thompson sampling, which uses each version in proportion to the probability that it's better.
3. **Hierarchical models:** sharing information between versions with hyperpriors, predictions for a new version, posterior predictive distributions, and a hierarchical model of batting averages for every player in Major League Baseball in 2023.

The notebook comes in two versions: one with blanks for the exercises, and one with solutions.

| Notebook | Exercises | Solutions |
|---|---|---|
| Bayesian Decision Analysis with PyMC | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BDAwithPyMC/blob/main/notebooks/01_beta_binomial.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BDAwithPyMC/blob/main/solutions/01_beta_binomial.ipynb) |

The version with blanks raises errors until you do the exercises.

### Data

* Batting statistics for every player with at least one at bat in Major League Baseball in 2023: `data/batting_2023.csv`, from Bill Engels's [tutorial on Gaussian processes](https://github.com/bwengals/pydata_global_2024_GPs).

## Recordings

I presented this workshop at PyData Global 2025, and it was the first session of the PyMC Labs course [Applied Bayesian Modeling](https://www.pymc-labs.com/courses/applied-bayesian-modeling). The code in the video is not the current version; the tag after the link is the version of the code that goes with it.

* [PyData Global 2025](https://www.youtube.com/watch?v=6yVIlWGNoGI): tag [`pydata-global-2025`](https://github.com/AllenDowney/BDAwithPyMC/tree/pydata-global-2025)

## Running the notebooks

The easiest way to run the notebook is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. Colab has everything the notebook needs except PreliZ, which the first code cell installs, and the notebook downloads the data it needs.

To run it on your own computer, you need Python 3.12 or later with Jupyter, PyMC 5, ArviZ, PreliZ, pandas, Matplotlib, and Graphviz. You can [download the code in this zip file](https://github.com/AllenDowney/BDAwithPyMC/archive/refs/heads/main.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/BDAwithPyMC
cd BDAwithPyMC
```

Then install the packages with pip:

```
pip install -r requirements-dev.txt
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate BDAwithPyMC
```

Then run `jupyter lab` and open `notebooks/01_beta_binomial.ipynb`.

## Next steps

To go further, read [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops). [Bayesian Decision Analysis](https://github.com/AllenDowney/BayesianDecisionAnalysis) is an earlier workshop on the same ideas, using grid methods instead of PyMC.

For a live, guided course that starts with this material, see [Applied Bayesian Modeling](https://www.pymc-labs.com/courses/applied-bayesian-modeling) from PyMC Labs.

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
