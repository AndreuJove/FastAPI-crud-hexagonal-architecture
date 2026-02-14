# For now Debian is better that Alpine
# https://pythonspeed.com/articles/alpine-docker-python/
FROM python:3.10.6-slim-buster

ENV PYTHONPATH=/code \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

WORKDIR /code

COPY requirements/requirements.txt .
RUN pip3 install -r requirements.txt

COPY src ./src

WORKDIR /code/src
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]