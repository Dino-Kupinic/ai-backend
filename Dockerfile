FROM python:3.12-slim

ARG PORT
ENV PORT=${PORT}

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install poetry

COPY pyproject.toml poetry.lock* /app/

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1
RUN poetry install --only main

COPY apps/api/src /app/src

EXPOSE ${PORT}

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]

