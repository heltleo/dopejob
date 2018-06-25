web: gunicorn activcar.wsgi:application --preload
worker: celery -A rental worker -l info --without-mingle --without-heartbeat
