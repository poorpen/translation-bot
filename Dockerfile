FROM python:3.11

ENV PIP_NO_CACHE_DIR=off\
   PIP_DISABLE_PIP_VERSION_CHECK=on\
   POETRY_VERSION=1.6.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR translation_bot
COPY pyproject.toml poetry.lock /translation_bot/
COPY ./src /translation_bot/src

RUN poetry config virtualenvs.create false
RUN poetry install --without dev,migrations

CMD ["python3.11", "-m", "src"]