#syntax=docker/dockerfile:1.2

FROM python:latest
RUN useradd --user-group --system --create-home --no-log-init nonroot
USER nonroot

COPY ./app /app

# Install requirements
RUN pip install pipenv requests mdutils PyGithub && pipenv sync

# Setup Environment Variables
RUN --mount=type=secret, id=github_token \
  cat /run/secrets/token

CMD ["python", "/app/main.py"]
