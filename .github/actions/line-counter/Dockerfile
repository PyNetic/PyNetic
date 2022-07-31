FROM python:latest

RUN apt-get update

COPY ./app .

# Install requirements
RUN pip install pipenv requests mdutils PyGithub && pipenv sync

# Setup Environment Variables
RUN --mount=type=secret, id=TOKEN \
  export TOKEN=$(cat /run/secrets/TOKEN) && \
  python genenv.py

CMD ["python", "main.py"]
