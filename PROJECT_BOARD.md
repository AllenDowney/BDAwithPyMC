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
- [x] Environment (2026-10-20): `mamba env create` of the full `environment.yml` timed out after 20 minutes; without the site build tools it took 53 s (the tools go in with `mamba install` in step 6). Python 3.12.15, PyMC 5.28.5, PyTensor 2.38.3, ArviZ 0.23.4, PreliZ 0.22.0, NumPy 2.4, pandas 3.0, Matplotlib 3.10.9, SciPy 1.18, numba 0.65

**1. Runs in a current environment**
- [x] `environment.yml` (Python 3.12, conda-forge, `pymc>=5.28,<6`, `arviz<1`, `matplotlib<3.11` as in SurveyDataPyMC, `preliz<0.23`, python-graphviz, pytest, nbmake, the site build tools), `requirements.txt` (the same, unpinned otherwise), `requirements-dev.txt`; root `Makefile` and `pixi.toml` deleted (2026-10-20)
- [x] Install cell: `%pip install -q "preliz<0.23"` if PreliZ is missing (Decisions: PreliZ). The notebook downloads `batting_2023.csv` (cell before the baseball model)
- [x] Breakage and warnings (2026-10-20): none. The solutions run with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors, and with no stderr output except PyMC's sampling messages. Not checked in a Colab-matched env (pandas 2.2, NumPy 2.1, ArviZ 0.22); the Colab run in step 3 covers it
- [x] `np.set_printoptions(legacy="1.25")` in the imports cell; solutions re-run and saved with outputs
- [x] Data URL: now this repo's `data/batting_2023.csv`; the downloaded copies are in `.gitignore`
- [x] Simulated campaigns seeded (`rng = np.random.default_rng(17)`, `pm.draw(dist, random_seed=rng)`); sampling not seeded (Decisions)
- [x] Title cell: links the PyMC Labs course page instead of `pymc-labs/pymc-workshop`; the PreliZ/Numba note dropped (Decisions)
- [x] Setup instructions in the README: Colab first, then pip or mamba (the rest of the README is step 5)

**2. Tests and CI**
- [x] `pytest --nbmake solutions/` (2026-10-20): passes, 34 s locally (80 s for a cold run). No fewer-draws hook: an IPython startup file that cut `pm.sample` to 200 + 200 saved only 30 s (most of the time is compiling) and added r-hat warnings, so it was dropped. The version with blanks isn't tested (Decisions); it fails in 13 cells until the exercises are done
- [x] `.github/workflows/tests.yml` (push to main, PR, monthly, manual; Python 3.12; apt Graphviz for `model_to_graphviz`; pip; 20-minute timeout; checkout@v5, setup-python@v6). First run passed in 1 min 24 s: https://github.com/AllenDowney/BDAwithPyMC/actions/runs/39502765773
- [x] Status badge in the README

**3. Colab**
- [x] "Click here to run this notebook on Colab" cell after the title; the solutions also link to the version with blanks. The generator (`remove_soln.py`) rewrites the cell for the version with blanks (2026-10-20)
- [ ] Colab links in the README's notebook table (step 5; the setup section already has both)
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [x] Typos, broken links (2026-10-20): codespell finds nothing; read all the markdown and code. Fixed: "for example that rate does not change" → "for example, that the rate", a link to Bill Engels's tutorial (the data used to download from it), single → double quotes in one cell (the 2025 style), trailing spaces. `np.set_printoptions(legacy="1.25")` was already in the notebook (cell 4); the duplicate added in step 1 removed
- [x] Everything else under "Content issues"; 5–9 decided and applied (2026-10-20)
- [x] Notebook layout (2026-10-20): title cell with a one-line subtitle (the PyMC Labs sentence); Colab cell; copyright ("2025–2026") and license (code MIT, text CC BY-NC-SA 4.0) in the last cell, replacing an empty one. The only H1 is the title. Same in both versions (made by the generator). nbconvert's timing metadata stripped (the generator drops it too)

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
- CI speed: measure first; a hidden hook only if it's slow (it isn't; see step 2).
- Seeds: seed the simulated data, not the sampling.
- Title cell: link the PyMC Labs course page; drop the Colab/Numba note.
- PreliZ: pin `preliz<0.23`. PreliZ 0.26+ needs PyTensor 3 (via `pytensor_distributions`), which breaks Colab's PyMC 5.28 (PyTensor 2.38); 0.23+ needs numba 0.62 (Colab has 0.61.2), which is where the "incompatible Numba" warning came from. 0.22 installs cleanly. Revisit when Colab moves to PyMC 6 / ArviZ 1 (as in SurveyDataPyMC).
- Tests: the solutions only.

### Content issues

(For Allen to decide.)

1. Resolved 2026-10-20 (Allen): the title cell links the course page, https://www.pymc-labs.com/courses/applied-bayesian-modeling. PyMC Labs links in the README: still undecided (workshops plan).
2. The README still says "Material for a workshop at PyData Global 2025" (step 5). Its setup section was rewritten in step 1.
3. Resolved 2026-10-20: yes. The pymc-workshop commit of the same day is "Update for January workshop" (`bf7013e`); no tag (Decisions).
4. Resolved 2026-10-20: `plan.md` "Future work" moved to Task 2.
5. Resolved 2026-10-20 (Allen): reworded. "Its mean is about 9%, a little above the observed conversion rate, 8%, because the prior pulls it up. The 94% HDI extends from about 4% to 15%." (Exact for Beta(10, 97): mean 9.3%, HDI 4.4% to 14.6%.)
6. Resolved 2026-10-20 (Allen): "…is asymptotically optimal: as the experiment goes on, its regret (the conversions lost by using inferior versions) grows as slowly as possible." The old sentence ("maximizes expected utility given current beliefs") describes the greedy choice; Thompson sampling matches the Lai–Robbins regret lower bound for Bernoulli bandits (Kaufmann, Korda & Munos 2012, https://arxiv.org/abs/1205.4217), and the Bayes-optimal policy for discounted reward is the Gittins index. The same sentence is in pymc-workshop `Session1-Prior_and_Posterior` (from 2025-08); not changed there.
7. Resolved 2026-10-20 (Allen): sections under each Part are `###`, all headings in sentence case.
8. Resolved 2026-10-20 (Allen): left as is ("speak for itself").
9. Resolved 2026-10-20 (Allen): `data/batting_2023.csv` had literal escapes (`P\xc3\xa9rez`, `O\'Neill`); now UTF-8, read with a plain `pd.read_csv` (checked: same DataFrame as the old two-step read). Old notebooks (the tags) still download the original from `bwengals/pydata_global_2024_GPs`.

---

## Task 2: A Gamma-Poisson notebook

**Status:** Pending (from `plan.md`, 2025-12; not part of the refresh)

- A notebook on the Gamma-Poisson and Gamma-Exponential models, with the same progression as `01_beta_binomial`: basic model → decision-making → hierarchical model. Separate notebooks for counts (Gamma-Poisson) and waiting times (Gamma-Exponential), or one.
- Examples: counts (customer service tickets, page views, defects, World Cup goals); waiting times (time between purchases, time to churn, failures, session length); hierarchical by store, segment, product category, or team.
- Business applications (high priority): customer lifetime value, inventory, churn, conversion funnels.
- Suggestion from the plan: start with Gamma-Poisson and a business example (support tickets or web analytics).
