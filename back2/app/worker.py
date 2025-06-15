from celery import Celery
from celery.schedules import crontab
import os

celery = Celery(
    'tasks',
    broker=os.getenv('REDIS_URL', 'redis://redis:6379/0'),
    backend=os.getenv('REDIS_URL', 'redis://redis:6379/0')
)

celery.conf.beat_schedule = {
    'fetch-daily-data': {
        'task': 'app.tasks.fetch_data',
        'schedule': crontab(hour=0, minute=0),  # Run at midnight every day
    },
}

celery.conf.timezone = 'UTC' 