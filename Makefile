PROJECT_NAME = BDAwithPyMC

create_environment:
	conda create -y -c conda-forge -n $(PROJECT_NAME) \
	    arviz \
	    "pytensor>=2.21.0" \
	    "pymc>=5.15.0"
	@echo ">>> conda env created. Activate with:\nconda activate $(PROJECT_NAME)"

requirements:
	python -m pip install -U pip setuptools wheel
	python -m pip install -r requirements.txt

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
