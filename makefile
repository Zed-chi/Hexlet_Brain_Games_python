install:
	poetry install

lint:
	poetry run flake8 brain_games

publish:
	poetry publish -r test