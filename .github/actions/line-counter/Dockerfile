#syntax=docker/dockerfile:1.2

FROM python:latest

COPY ./app /app

# Install requirements
RUN pip install pipenv requests mdutils PyGithub && pipenv sync \
  python genenv.py

# Setup Environment Variables
RUN --mount=type=secret, TOKEN=github_token \
  cat /run/secrets/token

CMD ["python", "/app/main.py"]
