install:
	poetry install

lint:
	poetry run flake8 brain-games
	poetry run flake8 brain-even
	poetry run flake8 brain-calc
	poetry run flake8 brain-gcd
	poetry run flake8 brain-progression
	poetry run flake8 brain-prime

publish:
	poetry build
	poetry publish -r test
