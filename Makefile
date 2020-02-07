install:
	poetry install

lint:
	poetry run flake8 ./brain_games

publish:
	poetry build
	poetry publish -r test
