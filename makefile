# Project Directory
SRC_DIR := app

# Default Rule
.DEFAULT_GOAL := help

# ============================================================================

help:  ## 💬 This is help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


run: venv ## 🏃 Run the server locally using Python & Flask
	. $(SRC_DIR)/.venv/bin/activate \
	&& python $(SRC_DIR)/app.py


lint: venv ## 🔎 Pep8 Check over the python codes
	. $(SRC_DIR)/.venv/bin/activate \
	&& flake8 $(SRC_DIR)/ --show-source --statistics


test: venv ## 🚦 Do unittesting over the project
	. $(SRC_DIR)/.venv/bin/activate \
	&& pytest $(SRC_DIR)/tests --junitxml=report.xml


coverage: venv ## 📜 Create test-coverage report as html file
	. $(SRC_DIR)/.venv/bin/activate \
	&& coverage run -m pytest \
	&& coverage html


clean:  ## 🧹 Clean up the project
	rm -rf $(SRC_DIR)/.venv
	rm -rf .coverage
	rm -rf report.xml
	find . -name .pytest_cache -type d -print0|xargs -0 rm -rf
	find . -name __pycache__ -type d -print0|xargs -0 rm -rf
	find . -name .mypy_cache -type d -print0|xargs -0 rm -rf


# ============================================================================

venv: $(SRC_DIR)/.venv/touchfile

$(SRC_DIR)/.venv/touchfile: $(SRC_DIR)/requirements.txt
	python3 -m venv $(SRC_DIR)/.venv
	. $(SRC_DIR)/.venv/bin/activate; pip install -Ur $(SRC_DIR)/requirements.txt
	touch $(SRC_DIR)/.venv/touchfile