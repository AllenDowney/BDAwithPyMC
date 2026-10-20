# BDAwithPyMC Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress

**Context:** BDAwithPyMC is a "current" workshop (GreenTeaPress Task 24). The guide is the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are worked examples. 15 stars. Given at PyData Global 2025 (2025-12-10; [recording](https://www.youtube.com/watch?v=6yVIlWGNoGI), 1:21) and as the first session of the PyMC Labs course Applied Bayesian Modeling. The notebook runs PyMC sampling, so CI must stay fast (fewer draws in tests if needed).

**0. Set up**
- [x] `git fetch`: pulled one commit (README: venues, recordings). Local edits and untracked files listed (Inventory, below), backed up to the session scratchpad (2026-10-20)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-20)
- [x] Tags created locally (2026-10-20): `pydata-global-2025` at `02f10e6` (2025-12-01, "Adding batting data"; the last commit before the event), `pre-refresh-2026` at `7e34a9b`
- [x] Tags pushed (2026-10-20). No tag for the PyMC Labs session (not publicly recorded)
- [x] Inventory (below)
- [ ] Environment: an old `BDAwithPyMC` conda env exists; recreate it from the new `environment.yml` in step 1

**1. Runs in a current environment**
- [ ] `environment.yml`, `requirements.txt`, `requirements-dev.txt`
- [ ] First code cell installs PreliZ if missing and downloads `batting_2023.csv` if missing
- [ ] Breakage and deprecation warnings (scratch runs with warnings as errors)
- [ ] `np.set_printoptions(legacy='1.25')`
- [ ] Data URL: the notebook downloads `batting_2023.csv` from a third-party repo (`bwengals/pydata_global_2024_GPs`); use the copy in this repo
- [ ] Setup instructions: Colab first, then pip or mamba

**2. Tests and CI**
- [ ] `pytest --nbmake`, with fewer draws in CI
- [ ] `.github/workflows/tests.yml`
- [ ] Status badge in the README

**3. Colab**
- [ ] "Click here to run this notebook on Colab" cell; the solution notebook links to the version with blanks
- [ ] Colab links in the README's notebook table
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Typos, wrong docstrings, broken links (codespell, and read the markdown), in both versions
- [ ] Everything else under "Content issues"
- [ ] Notebook layout: title cell, Colab cell, copyright and license at the end

**5. README in the standard shape**
- [ ] README rewritten

**6. Site and visibility**
- [ ] `jb/` site (none yet; GitHub Pages is off)
- [ ] SEO checklist in a test build; Allen approves the descriptions
- [ ] Publish; `Sitemap:` line in `~/AllenDowney.github.io/robots.txt`; Search Console
- [ ] Hub entry, repo description and topics

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

### Inventory (2026-10-20)

**The workshop:** one notebook, in two versions.

| Notebook | Topic | Imports, files |
|---|---|---|
| `solutions/01_beta_binomial.ipynb` (solutions, saved with outputs, 161 cells) | Beta-binomial A/B testing, Thompson sampling, hierarchical model (batting averages) | arviz, numpy, matplotlib, pandas, pymc, preliz (installed if missing), graphviz; downloads `batting_2023.csv` |
| `notebooks/01_beta_binomial.ipynb` (with blanks, no outputs, 157 cells) | same | same |

The student version is made from the solutions by `notebooks/remove_soln.py` (drops code cells that start with `# Solution`, clears outputs), run by `notebooks/Makefile` (which also commits). Both files were untracked; now kept (Decisions), without the Makefile's auto-commit and the `_soln` by-product. Checked: it reproduces the committed student version exactly.

The notebook has 8 `pm.sample()` calls (default 1000 tune + 1000 draws, 4 chains) and two `sample_prior_predictive`. No random seed, so outputs change on every run.

**Other files:**
- `data/batting_2023.csv` (committed; same file as the copies in `notebooks/` and `solutions/`, which are untracked downloads). The notebook downloads from `bwengals/pydata_global_2024_GPs`, not from this repo.
- `environment.yml` (unpinned Python, pip for most packages), `requirements.txt`, root `Makefile` (conda env), `pixi.toml`: four ways to set up.
- `LICENSE` (MIT).

**Local state not in git (2026-10-20; backups in the session scratchpad; all discarded except the generator, Decisions):**
- Modified: `solutions/01_beta_binomial.ipynb`, outputs only (a re-run; the cell sources are the same as HEAD).
- Untracked:
  - `notebooks/Makefile`, `notebooks/remove_soln.py`: the tool that makes the student version (keep?).
  - `notebooks/01_beta_binomial_soln.ipynb`: a by-product of `remove_soln.py` (the solution cells and headings only).
  - `plan.md`: notes from the 2025 draft, all done, plus "Future work" (a Gamma-Poisson notebook).
  - `solutions/01_beta_binomial.md`: a jupytext copy of the solutions, out of date (73 code cells vs. 83).
  - `notebooks/batting_2023.csv`, `solutions/batting_2023.csv`: downloads.
  - `.vscode/settings.json`, `.ipynb_checkpoints/`.

### Decisions

(Allen, 2026-10-20)

- Local files: keep `notebooks/remove_soln.py` and `notebooks/Makefile` (no auto-commit). Discard the re-run outputs, the jupytext `.md`, the `_soln` by-product, the CSV copies, `.vscode/` (now in `.gitignore`) and the checkpoints. `plan.md` deleted; its "Future work" is Task 2.
- Tags: push `pydata-global-2025` and `pre-refresh-2026`; no tag for the PyMC Labs session.
- Setup: the checklist standard (`environment.yml`, `requirements.txt`, `requirements-dev.txt`); delete the root `Makefile` and `pixi.toml` (step 1).
- Layout: keep `notebooks/` (with blanks) and `solutions/`, so the Colab links in the video keep working.

### Content issues

(For Allen to decide.)

1. The title cell says the notebook "is based on the first notebook of the Bayesian Modeling Workshop offered by PyMC Labs" and links `pymc-labs/pymc-workshop` (a private repo?). Workshops plan: PyMC Labs links in READMEs are undecided.
2. The README still says "Material for a workshop at PyData Global 2025" and the setup section uses the root `Makefile` and conda.
3. Two commits on 2026-01-09 (after PyData Global) changed the notebook: a note about installing PreliZ on Colab, `az.plot_posterior(diff)` without `var_names`, and dropped comments on the hyperpriors. Were these for the PyMC Labs session?
4. Resolved 2026-10-20: `plan.md` "Future work" moved to Task 2.

---

## Task 2: A Gamma-Poisson notebook

**Status:** Pending (from `plan.md`, 2025-12; not part of the refresh)

- A notebook on the Gamma-Poisson and Gamma-Exponential models, with the same progression as `01_beta_binomial`: basic model → decision-making → hierarchical model. Separate notebooks for counts (Gamma-Poisson) and waiting times (Gamma-Exponential), or one.
- Examples: counts (customer service tickets, page views, defects, World Cup goals); waiting times (time between purchases, time to churn, failures, session length); hierarchical by store, segment, product category, or team.
- Business applications (high priority): customer lifetime value, inventory, churn, conversion funnels.
- Suggestion from the plan: start with Gamma-Poisson and a business example (support tickets or web analytics).
