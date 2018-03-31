release: pipenv run python manage.py init_db
web: gunicorn app:app --log-file - --workers=2