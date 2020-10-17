FROM python:3.8.6

ARG allow_hosts="*"
ENV ALLOWED_HOSTS=$allow_hosts
ARG django_secret="SECRET_KEY"
ENV SECRET_KEY=$django_secret
ARG database_secret=""
ENV DB_PASS=$database_secret
ARG debug="True"
ENV DEBUG_MODE=$debug

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN python ./manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0", "--workers=4", "backend.wsgi:application"]
