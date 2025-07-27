FROM python:3.13-bullseye

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev,test && rm -rf $POETRY_CACHE_DIR

COPY app ./app

EXPOSE 8080

ENTRYPOINT ["poetry", "run", "python", "-m", "app.main"]