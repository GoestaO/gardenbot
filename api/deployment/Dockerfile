FROM ubuntu:latest
FROM python:3
MAINTAINER Gösta "goesta.o@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential libglib2.0-dev python3-RPi.GPIO
COPY . /gardenbot-api
COPY
WORKDIR /gardenbot-api
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
CMD ["main.py"]