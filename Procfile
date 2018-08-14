web: gunicorn project.wsgi:application --preload
worker: celery -A project worker beat -l info --without-mingle --without-heartbeat
