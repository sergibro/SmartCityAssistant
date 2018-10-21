FROM python:latest

RUN apt-get -y update
RUN apt-get install -y python-pip
ADD requirements.txt .
RUN pip install -r requirements.txt --upgrade

WORKDIR /app