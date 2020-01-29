FROM python:3.7-alpine
MAINTAINER Vojtech Janousek

ENV PYTHONUNBUFFERED 1

RUN mkdir /djangoapp
WORKDIR /djangoapp
COPY . /djangoapp/

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

EXPOSE 8000

RUN adduser -D user
USER user
