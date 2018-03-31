release: pipenv run python manage.py init_db
web: gunicorn app:app --log-file - --worker-class=meinheld.gmeinheld.MeinheldWorker --workers=2