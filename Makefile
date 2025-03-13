install:
	pip install --upgrade pip && pip install -r requirements.txt 

test:
	python -m pytest lib/tests/test_*.py 
	ls  node/*.ipynb | xargs -I {} bash -c "py.test --nbval-lax '{}'"
	ls  linked-lists/*.ipynb | xargs -I {} bash -c "py.test --nbval-lax '{}'"

format:
	black lib

lint:
	pylint --disable=R,C,W0702,W0621,W1203 lib

refactor: format lint test

jupyter9:
	jupyter notebook
