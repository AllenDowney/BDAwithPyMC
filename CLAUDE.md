# BDAwithPyMC

Allen Downey's workshop "Bayesian Decision Analysis with PyMC: Beyond A/B Testing": Bayesian A/B testing with the beta-binomial model, Thompson sampling, and a hierarchical model, in PyMC, ArviZ and PreliZ. Given at PyData Global 2025 (2025-12-10) and as the first session of the PyMC Labs course Applied Bayesian Modeling.

**Guide for the 2026 refresh:** the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md` (BayesMadeSimple and CompStats are worked examples). Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the workshop

- `solutions/01_beta_binomial.ipynb`: the source, with solutions, saved with outputs.
- `notebooks/01_beta_binomial.ipynb`: the version with blanks, made from the solutions by `notebooks/remove_soln.py` (drops code cells that start with `# Solution`, clears outputs). Edit the solutions, then regenerate.

Data: `data/batting_2023.csv` (MLB batting, 2023).

## Site

`jb/` builds the Jupyter Book site at `allendowney.github.io/BDAwithPyMC/` (`cd jb; ./build.sh [publish]`, published to `gh-pages`). `prep_notebooks.py` copies the solutions in as `beta_binomial.ipynb`, renames the H1 and holds the page description. The build doesn't execute the notebook: re-run and save the solutions first. Delete `jb/_build/` before publishing. Template: BayesMadeSimple.

## Tags

- `pydata-global-2025`: the code in the PyData Global 2025 recording (the last commit before the event).
- `pre-refresh-2026`: the state before the 2026 refresh.

## Testing

Environment: `mamba env create -f environment.yml` (name `BDAwithPyMC`). Tests: `pytest --nbmake solutions/` (about 1 minute; CI in `.github/workflows/tests.yml`). The version with blanks isn't tested; it fails until the exercises are done.

Keep PyMC 5 / ArviZ 0.x and `preliz<0.23` while Colab has PyMC 5.28 (see `PROJECT_BOARD.md`, Decisions). After editing the solutions, run them, save them with outputs, and regenerate the version with blanks (`cd notebooks; make`).
