FROM python:3.8.6

ARG allow_hosts="*"
ENV ALLOWED_HOSTS=$allow_hosts
ARG django_secret="SECRET_KEY"
ENV SECRET_KEY=$django_secret
ARG database_secret=""
ENV DB_PASS=$database_secret
ARG debug="False"
ENV DEBUG_MODE=$debug
ARG django_config="backend.settings_prod"
ENV DJANGO_SETTINGS_MODULE=$django_config

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python ./manage.py migrate

EXPOSE 8000
# CMD ["gunicorn", "--bind=0.0.0.0", "--workers=4", "backend.wsgi:application"]
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
