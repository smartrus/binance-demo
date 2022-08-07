FROM ubuntu:20.04
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install python3 python3-pip

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

ENV FLASK_APP=web.app
ENV FLASK_DEBUG=1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /opt
