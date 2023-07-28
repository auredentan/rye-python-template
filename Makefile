include ./help.mk

# Use a standard bash shell, avoid zsh or fish
SHELL:=/bin/bash

# Select the default target, when you are simply running "make"
.DEFAULT_GOAL:=help

# Use python executables inside venv
export PATH := ./venv/bin:$(PATH)

.PHONY: dev format lint sql.autogenerate sql.upgrade

init:
	python3 -m venv venv
	venv/bin/pip install pip-tools

sync:
	pip-sync requirements.txt

upgrade-deps:
	pip-compile \
		--quiet --generate-hashes --max-rounds=20 --strip-extras \
		--resolver=backtracking \
		--output-file requirements.txt \
		requirements.in

dev:
	uvicorn src.app.main:app --reload

lint:
	black --check -q src
	ruff check src
	mypy src
	isort src -c

format:
	black src
	isort src

tests:
	pytest

sql.autogenerate:
	alembic revision --autogenerate

sql.upgrade:
	alembic upgrade head
