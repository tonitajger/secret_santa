run:
	python secret_santa/src/main.py

install_deps:
	pip install -r requirements.txt

test:
	python -m pytest