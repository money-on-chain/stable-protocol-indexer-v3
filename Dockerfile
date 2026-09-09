FROM python:3.10-slim

LABEL maintainer='martin.mulone@moneyonchain.com'

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /home/www-data && mkdir /home/www-data/app && useradd -r -d /home/www-data appuser

ARG CONFIG=config.json

WORKDIR /home/www-data/app/
COPY app_run_indexer.py ./
COPY $CONFIG ./config.json
COPY indexer/ ./indexer/

ENV PATH="$PATH:/home/www-data/app/"
ENV AWS_DEFAULT_REGION=us-west-1

ENV PYTHONPATH="/home/www-data/app/"

USER appuser

CMD [ "python", "./app_run_indexer.py" ]
