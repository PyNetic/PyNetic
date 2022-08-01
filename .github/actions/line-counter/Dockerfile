FROM python:3.10

RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update && \
  apt-get upgrade -y

RUN pip install --no-input --upgrade pip

RUN pip install requests mdutils PyGithub

COPY ./app /app

CMD python /app/main.py
