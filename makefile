# Project Directory
SRC_DIR := app

# Default Rule
.DEFAULT_GOAL := help


help:  ## 💬 This is help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

lint: ## 🎯 Pep8 Check over the python codes
	flake8 $(SRC_DIR)/ --show-source --statistics	

test: ## 🚦 Do unittesting over the project
	pytest $(SRC_DIR)/tests/

run: venv ## 🏃 Run the server locally using Python & Flask
	. .venv/bin/activate \
	&& python $(SRC_DIR)/app.py

clean:  ## 🧹 Clean up the project
	rm -rf $(SRC_DIR)/.venv
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf $(SRC_DIR)/tests/__pycache__
	rm -rf $(SRC_DIR)/.pytest_cache
	rm -rf ./.venv	
	rm -rf ./__pycache__	
	rm -rf ./.idea	
	rm -rf .pytest_cache


venv: .venv/touchfile
.venv/touchfile: $(SRC_DIR)/requirements.txt
	python3 -m venv .venv
	. .venv/bin/activate; 
	pip install -Ur $(SRC_DIR)/requirements.txt
	touch .venv/touchfile	