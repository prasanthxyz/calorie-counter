cd backend
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python ./manage.py migrate
gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 backend.wsgi:application --access-logfile '-' --error-logfile '-'
