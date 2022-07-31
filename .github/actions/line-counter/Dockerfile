#syntax=docker/dockerfile:1.2

FROM python:latest
RUN useradd -rm -d /home/nonroot -s /bin/bash -g root -G sudo -u 1001 nonroot
USER nonroot

COPY ./app /home/nonroot/app

ENV PATH="${PATH}:/home/nonroot/.local/bin/"

# Install requirements
RUN pip install pipenv requests mdutils PyGithub && pipenv sync \
  python genenv.py

# Setup Environment Variables
ENV TOKEN ${github_token?tokennotset}

CMD ["python", "/home/nonroot/app/main.py"]
