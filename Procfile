web: gunicorn activcar.wsgi:application --preload
worker: celery -A activcar worker -l info --without-mingle --without-heartbeat
