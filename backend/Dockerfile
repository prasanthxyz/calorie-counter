FROM python:3.6

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install vim git -y --no-install-recommends
RUN git clone https://github.com/prasanthxyz/calorie-counter.git
WORKDIR /code/calorie-counter/backend

RUN pip install -r requirements.txt
RUN python ./manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0", "--workers=4", "backend.wsgi:application"]
