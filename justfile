install:
  poetry install --no-root --all-extras

fix-lock:
    poetry lock

dev-api:
  uvicorn apps.api.src.main:app --reload

dev-docs:
    cd docs && pnpm run docs:dev

dev-examples-nuxt:
  cd examples/web-nuxt && pnpm run dev

test:
  pytest

release:
    semantic-release publish
