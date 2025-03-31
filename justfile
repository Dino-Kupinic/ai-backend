install:
  poetry install --no-root --all-extras

dev-api:
  uvicorn apps.api.src.main:app --reload

dev-examples-nuxt:
  cd examples/web-nuxt && pnpm run dev

test:
  pytest
