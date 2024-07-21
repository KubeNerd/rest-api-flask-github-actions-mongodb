APP = restapi

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings
compose:
	@docker compose up -d
	@docker compose down