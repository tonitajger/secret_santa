.PHONY: run
run:
	python secret_santa/src/main.py

.PHONY: install-src-deps
install-src-deps:
	pip install -r secret_santa/src/requirements.txt

.PHONY: install-test-deps
install-test-deps:
	pip install -r secret_santa/tests/requirements.txt

.PHONY: install-local-deps
install-local-deps: install-test-deps install-src-deps

.PHONY: test
test:
	coverage run -m pytest secret_santa/
	coverage report -m

.PHONY: type-check
type-check:
	python -m mypy secret_santa/src

.PHONY: build
build: test type-check
