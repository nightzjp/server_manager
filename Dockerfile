FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Shanghai

WORKDIR /app

COPY . /app

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

RUN apt-get update \
  && apt-get install -y procps net-tools apt-utils \
  && ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone \
  && pip install pipenv -i https://mirrors.aliyun.com/pypi/simple/

RUN pipenv sync  && pipenv install --dev

RUN chmod +x /app/start.sh

CMD ["sh", "start.sh"]
