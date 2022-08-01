FROM python:3.10

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get autoremove && \
  apt-get autoclean \
  pip install --no-input --upgrade pip

RUN pip install requests mdutils PyGithub

COPY ./app /app

CMD python /app/main.py
