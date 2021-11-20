.PHONY: run
run:
	python secret_santa/src/main.py --input_path input/participants.txt

.PHONY: run_write_output
run_write_output:
	python secret_santa/src/main.py --input_path input/participants.txt --output_dir output/results

.PHONY: install_src_deps
install_src_deps:
	pip install -r secret_santa/src/requirements.txt

.PHONY: install_test_deps
install-test-deps:
	pip install -r secret_santa/tests/requirements.txt

.PHONY: install_local_deps
install_local_deps: install_test_deps install_src_deps

.PHONY: test
test:
	coverage run -m pytest secret_santa/
	coverage report -m

.PHONY: type-check
type-check:
	python -m mypy secret_santa/src

.PHONY: build
build: test type-check
