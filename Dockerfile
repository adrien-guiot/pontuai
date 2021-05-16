# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /pontuAI
WORKDIR $APP_HOME
COPY . ./

# Install dependencies.
RUN pip install Flask gunicorn


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 pontuAI:app