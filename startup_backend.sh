cd backend
apt-get update && apt-get install -y --no-install-recommends gcc libmysqlclient-dev python-dev
# sudo apt-get install gcc python3-mysqldb libmysqlclient-dev python-dev
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python ./manage.py migrate
gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 backend.wsgi:application --access-logfile '-' --error-logfile '-'
