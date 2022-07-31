FROM python:latest

COPY ./app /app

RUN pip install pipenv requests mdutils PyGithub && pipenv sync \
  --mount=type=secret, GITHUB_TOKEN=token \
  --mount=type=secret, ACTION_TOKEN=standard_token \
  python genenv.py

CMD ["python", "/app/main.py"]
