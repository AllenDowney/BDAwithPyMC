# Bayesian Decision Analysis with PyMC

[![tests](https://github.com/AllenDowney/BDAwithPyMC/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/BDAwithPyMC/actions/workflows/tests.yml)


[Here is the video of the workshop](https://www.youtube.com/watch?v=6yVIlWGNoGI) (PyData Global 2025). This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops).


Material for a workshop at [PyData Global 2025](https://pydata.org/global2025)

**Bayesian Decision Analysis with PyMC: Beyond A/B Testing**


## Overview

This hands-on tutorial introduces practical Bayesian inference using PyMC, with a focus on A/B testing, decision-making under uncertainty, and hierarchical modeling. Through real-world examples you'll learn how to build and interpret Bayesian models, evaluate competing hypotheses, and implement adaptive strategies such as Thompson sampling.

These techniques are useful across domains (marketing, healthcare, public policy, UX, and general data science) for experimentation, decision-making, and evidence-based analysis.

## What you'll learn

- How to formulate simple Bayesian models for A/B testing
- How to interpret posterior distributions and high-density intervals
- How to apply Thompson sampling for adaptive experiments
- How to build hierarchical models for partial pooling and improved prediction
- How to use PyMC and ArviZ for Bayesian modeling and model checking

## Topics and Examples

### Bayesian A/B Testing (Beta-Binomial)

- Represent prior beliefs with the Beta distribution
- Use Binomial likelihoods to model observed outcomes
- Compute and interpret posterior distributions and credible intervals

### Bayesian Bandits and Thompson Sampling

- Estimate the probability that one version outperforms another (beyond p-values)
- Use Thompson sampling to guide decisions in adaptive experiments
- Simulate and visualize an adaptive email campaign example

### Hierarchical Models (Partial Pooling)

- Share information across variants using hierarchical priors
- Use posterior predictive distributions to quantify uncertainty
- Understand second-order probabilities and shrinkage

### Hands-On Learning

Participants follow along in Jupyter notebooks (hosted on Colab — no installation required). Exercises are embedded with guided solutions. Code relies on PyMC, ArviZ, and standard scientific Python libraries.

### Prerequisites

- Intermediate Python: basic familiarity with NumPy, plotting, and Jupyter notebooks
- No prior Bayesian statistics or PyMC experience required

### Instructor

**Allen Downey** — Principal Data Scientist at PyMC Labs and Professor Emeritus at Olin College. Author of *Think Python*, *Think Bayes*, and *Probably Overthinking It*. Allen holds a Ph.D. in Computer Science from UC Berkeley and degrees from MIT.



## Running the notebooks

### On Colab (recommended)

Colab needs no installation:

- [Open the notebook (with blanks for the exercises) on Colab](https://colab.research.google.com/github/AllenDowney/BDAwithPyMC/blob/main/notebooks/01_beta_binomial.ipynb)
- [Open the notebook (with solutions) on Colab](https://colab.research.google.com/github/AllenDowney/BDAwithPyMC/blob/main/solutions/01_beta_binomial.ipynb)

Colab has everything the notebook needs except PreliZ, which the first code cell installs. The notebook downloads the data it needs.

The version with blanks raises errors until you do the exercises.

### On your computer

Clone the repository (or [download it as a zip file](https://github.com/AllenDowney/BDAwithPyMC/archive/refs/heads/main.zip)):

```bash
git clone https://github.com/AllenDowney/BDAwithPyMC.git
cd BDAwithPyMC
```

Then either install the requirements with pip (Python 3.12 or later):

```bash
pip install -r requirements-dev.txt
```

or create a conda environment with [mamba](https://mamba.readthedocs.io/) (or conda):

```bash
mamba env create -f environment.yml
mamba activate BDAwithPyMC
```

and run `jupyter lab`.
