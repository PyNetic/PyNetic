FROM python:latest

RUN pip install requests PyGithub

COPY ./app /app

RUN pip install pipenv && pipenv sync

RUN --mount=type=secret, TOKEN=GITHUB_TOKEN \
  python genenv.py

CMD ["python", "/app/main.py"]
