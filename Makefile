install:
	pip install --upgrade pip && pip install -r requirements.txt 

test:
	find . -maxdepth 2 -type f -name "*.ipynb" | xargs -I {} bash -c "py.test  --maxfail=1 --nbval-lax '{}'"

format:
	find . -maxdepth 2 -type f -name "*.ipynb" | xargs -I {} bash -c "black '{}'"

refactor: format test

jupyter9:
	jupyter notebook
