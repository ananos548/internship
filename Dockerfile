FROM python:3.10

COPY req.txt /temp/req.txt
COPY internship /internship
WORKDIR /internship
EXPOSE 8000

RUN apt-get update && apt-get install -y postgresql-client build-essential libpq-dev
RUN pip install --upgrade pip
RUN pip install -r /temp/req.txt


RUN adduser --disabled-password app

RUN chown -R app:app /internship

USER app