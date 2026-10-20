NOTEBOOK = 01_beta_binomial.ipynb
SOLUTIONS_DIR = ../solutions

.PHONY: all

# Make the version with blanks from the solutions
all:
	cp $(SOLUTIONS_DIR)/$(NOTEBOOK) $(NOTEBOOK)
	python remove_soln.py $(NOTEBOOK)
