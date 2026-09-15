# ==============================================================================
# Real-Time E-Commerce Insights Engine - Makefile for Students & Developers
# ==============================================================================

.PHONY: help install data run test lint format docker-build docker-up docker-down clean

PYTHON ?= python3
VENV ?= .venv
BIN = $(VENV)/bin

help: ## Show this help message with available commands
	@echo "================================================================"
	@echo " Real-Time E-Commerce Insights Engine - Available Commands:"
	@echo "================================================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

venv: ## Create a local virtual environment (.venv)
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created in $(VENV). Activate with: source $(VENV)/bin/activate"

install: ## Install all runtime and testing dependencies
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt ruff

data: ## Generate mock e-commerce sales dataset
	$(BIN)/python app/generate_data.py

run: ## Run the local FastAPI development server with hot-reload
	$(BIN)/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test: ## Execute test suite using pytest
	$(BIN)/pytest -v

lint: ## Check code for errors and styling issues with Ruff
	$(BIN)/ruff check .

format: ## Format Python code with Ruff
	$(BIN)/ruff format .

docker-build: ## Build the Docker image
	docker compose build

docker-up: ## Start the application stack using Docker Compose
	docker compose up --build

docker-down: ## Stop and remove running Docker containers
	docker compose down

clean: ## Clean up temporary files, pycache, and caches
	rm -rf __pycache__ app/__pycache__ tests/__pycache__
	rm -rf .pytest_cache .ruff_cache reports
	find . -type f -name "*.pyc" -delete
