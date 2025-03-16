fmt:
    uv run ruff format

lint:
    uv run ruff check

fix:
    uv run ruff check --fix

run:
    uv run main.py