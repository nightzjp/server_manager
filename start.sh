#!/bin/bash

#pipenv run python manage.py migrate
#pipenv run python manage.py runserver 0.0.0.0:8000


if [ "$1" ]; then
  if [ "$1" = 'celery-beta' ]; then
    echo "pipenv run python manage.py migrate"
    echo "pipenv run celery -A face_safe beat --loglevel=INFO"
  elif [ "$1" = 'celery-worker' ]; then
    echo "pipenv run python manage.py migrate"
    echo "pipenv run celery -c 4 -A face_safe worker --loglevel=INFO"
  else
    echo "pipenv run python manage.py migrate"
    echo "pipenv run python manage.py $1"
  fi
else
  echo "default"
  echo "pipenv run python manage.py migrate"
  echo "pipenv run python manage.py runserver 0.0.0.0:8000"
fi
