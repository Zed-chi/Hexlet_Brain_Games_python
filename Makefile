install:
	poetry install

lint:
	poetry run flake8 brain-games

publish:
	poetry build
	poetry publish -r test
