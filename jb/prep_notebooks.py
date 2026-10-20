"""Copy the solution notebook into jb/ and prepare it for the book.

Writes beta_binomial.ipynb here from ../solutions/01_beta_binomial.ipynb:
- the H1 becomes TITLE, so the page title differs from the site title;
- the Colab cell stays (it links to the version with blanks);
- the page description goes in the notebook metadata (see GreenTeaPress plans/seo.md).
"""

import nbformat

SOURCE = '../solutions/01_beta_binomial.ipynb'
NAME = 'beta_binomial'
TITLE = 'A/B testing, bandits, and hierarchical models'
DESCRIPTION = ("Bayesian A/B testing in Python with PyMC: estimate conversion rates with the "
               "beta-binomial model, then use Thompson sampling and hierarchical models.")


nb = nbformat.read(SOURCE, 4)
first = nb.cells[0]
assert first.source.startswith('# Bayesian Decision Analysis with PyMC\n')
first.source = first.source.replace('# Bayesian Decision Analysis with PyMC', f'# {TITLE}', 1)

nb.metadata['myst'] = {'html_meta': {'description': DESCRIPTION}}
nb.metadata['og:description'] = DESCRIPTION
nbformat.write(nb, f'{NAME}.ipynb')
print(f'{NAME}: {TITLE} ({len(DESCRIPTION)} characters)')
