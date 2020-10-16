cd backend
pip install -r requirements.txt
python ./manage.py migrate
gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 backend.wsgi:application --access-logfile '-' --error-logfile '-'