FROM python:latest

COPY ./app /app

RUN pip install pipenv requests mdutils PyGithub && pipenv sync \
  --mount=type=secret, TOKEN=GITHUB_TOKEN \
  python genenv.py

CMD ["python", "/app/main.py"]
