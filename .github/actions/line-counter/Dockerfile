FROM python:latest

COPY ./app /app

# Install requirements
RUN pip install pipenv requests mdutils PyGithub && pipenv sync \
  python genenv.py

# Setup Environment Variables
RUN --mount=type=secret, GITHUB_TOKEN=token
RUN --mount=type=secret, ACTION_TOKEN=standard_token

CMD ["python", "/app/main.py"]
