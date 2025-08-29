fmt:
    uv run ruff format
    bun run biome check --formatter-enabled=true --organize-imports-enabled=true --write .

lint:
    uv run ruff check
    bun run biome ci

fix:
    uv run ruff check --fix
    bun run biome check --formatter-enabled=true --linter-enabled=true --organize-imports-enabled=true --write .

run:
    uv run main.py