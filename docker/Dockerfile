FROM python:latest

RUN apt-get -y update
RUN apt-get install -y python-pip
RUN pip install -r requirements.txt --upgrade

WORKDIR /app