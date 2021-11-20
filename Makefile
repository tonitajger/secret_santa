run:
	python secret_santa/src/main.py

install_deps:
	pip install -r requirements.txt

test:
	coverage run -m pytest secret_santa/
	coverage report -m

type-check:
	python -m mypy secret_santa/src

build:
	test
	type-check
