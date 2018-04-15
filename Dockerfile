FROM python:3.6-slim

ADD . /code
WORKDIR /code

ENV APP_SETTINGS=app.config.ProductionConfig

RUN pip install -i https://mirrors.aliyun.com/pypi/simple pipenv
RUN pipenv install --system