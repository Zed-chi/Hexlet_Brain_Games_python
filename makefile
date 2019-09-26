install:
	poetry install
publish:
	poetry publish -r test
lint:
	poetry run flake8 brain_games
