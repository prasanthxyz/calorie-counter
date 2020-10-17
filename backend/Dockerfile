FROM python:3.8.6

ARG allow_hosts="*"
ENV ALLOWED_HOSTS=$allow_hosts
ARG django_secret="SECRET_KEY"
ENV SECRET_KEY=$django_secret
ARG database_secret=""
ENV DB_PASS=$database_secret

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install vim git -y --no-install-recommends
RUN git clone https://github.com/prasanthxyz/calorie-counter.git
WORKDIR /code/calorie-counter/backend

RUN pip install -r requirements.txt
RUN python ./manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0", "--workers=4", "backend.wsgi:application"]
