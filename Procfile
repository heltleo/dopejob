web: gunicorn activcar.wsgi:application --preload
worker: celery -A activcar worker beat -l info --without-mingle --without-heartbeat
