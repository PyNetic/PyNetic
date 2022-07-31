#syntax=docker/dockerfile:1.2

FROM python:latest
USER nonroot

COPY ./app /app

# Install requirements
RUN pip install pipenv requests mdutils PyGithub && pipenv sync \
  python genenv.py

# Setup Environment Variables
ENV TOKEN ${github_token?tokennotset}

CMD ["python", "/app/main.py"]
