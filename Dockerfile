FROM python:3.7

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

ENV FLASK_APP=web.app
ENV FLASK_DEBUG=1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /opt
