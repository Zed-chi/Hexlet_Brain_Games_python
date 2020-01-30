install:
	poetry install

lint:
	poetry run flake8 brain-games
	poetry run flake8 brain-even

publish:
	poetry publish -r test
