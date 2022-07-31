FROM python:latest

RUN apt-get update

COPY ./app .

# Install requirements
RUN pip install requests mdutils PyGithub

# Setup Environment Variables
ENV TOKEN=$token

CMD ["python", "main.py"]
