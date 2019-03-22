FROM python:3.6-alpine

MAINTAINER Borja "borja.d.arevalo@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt
RUN mkdir /movies_app

WORKDIR /movies_app

COPY ./movies_app /movies_app

RUN adduser -D user
USER user
