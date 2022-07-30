FROM python:latest

COPY ./app /app

RUN pip install pipenv requests mdutils PyGithub && pipenv sync \
  --mount=type=secret, GITHUB_TOKEN=GITHUB_TOKEN \
  --mount=type=secret, ACTION_TOKEN=ACTION_TOKEN \
  python genenv.py

CMD ["python", "/app/main.py"]
