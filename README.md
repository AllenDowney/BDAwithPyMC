# Bayesian Decision Analysis with PyMC

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


## Setup Instructions

### Recommended: Google Colab (No Installation Required)

We **strongly recommend** running the notebooks on Google Colab, which requires no local installation:

- [Open notebook (no solutions) in Colab](https://colab.research.google.com/github/AllenDowney/BDAwithPyMC/blob/main/notebooks/01_beta_binomial.ipynb)
- [Open notebook (with solutions) in Colab](https://colab.research.google.com/github/AllenDowney/BDAwithPyMC/blob/main/solutions/01_beta_binomial.ipynb)

The default Colab environment has everything we need except Preliz, which will get installed automatically when you run the notebook.

If you run the notebook without solutions, you will get errors because some of the examples don't run unless you have completed the exercises.


### Alternative: Local Installation with Conda

If you prefer to run locally, we recommend using conda and the provided Makefile:

1. **Create the conda environment:**
   ```bash
   make create_environment
   ```

2. **Activate the environment:**
   ```bash
   conda activate BDAwithPyMC
   ```

3. **Install remaining requirements:**
   ```bash
   make requirements
   ```

The Makefile will:
- Create a conda environment with core packages (ArviZ, PyTensor, PyMC)
- Install additional dependencies from `requirements.txt` (Jupyter, Matplotlib, PreliZ, etc.)

