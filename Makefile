check:
	poetry run black src
	poetry run isort src/*.py
	poetry run mypy src
	poetry run flake8 src

