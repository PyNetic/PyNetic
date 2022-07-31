#syntax=docker/dockerfile:1.2

FROM python:latest
USER nonroot

COPY ./app /app

# Install requirements
RUN pip install pipenv requests mdutils PyGithub && pipenv sync

# Setup Environment Variables
RUN --mount=type=secret, id=TOKEN \
  export TOKEN=$(cat /run/secrets/TOKEN) \
  python genenv.py

CMD ["python", "/app/main.py"]
