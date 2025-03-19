.PHONY: setup clean test lint type-check format check-all

# Variables
PYTHON := python3
VENV := venv
BIN := $(VENV)/bin
SRC_DIR := src
NB_DIR0 := nb-ds
NB_DIR1 := nb-experiments
TEST_DIR := tests

help:
	@echo "Available commands:"
	@echo "  make setup         - Create virtual environment and install dependencies"
	@echo "  make clean        - Remove virtual environment and cache files"
	@echo " "
	@echo "  make test         - Run all tests"
	@echo " "
	@echo "  make lint         - Run pylint"
	@echo "  make type-check   - Run mypy type checking"
	@echo "  make format       - Format code with black"
	@echo "  make refactor     - Run all checks"

setup:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf **/__pycache__


test:
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR) -v

lint:
	$(BIN)/pylint $(SRC_DIR) $(TEST_DIR)

type-check:
	$(BIN)/mypy $(SRC_DIR) $(TEST_DIR)

format:
	$(BIN)/black $(SRC_DIR) $(TEST_DIR) $(NB_DIR0) $(NB_DIR1)
 

refactor: format lint type-check test 
