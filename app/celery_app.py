from celery import Celery

celery_app = Celery(
    "file_monitor",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["app.tasks"]
)

celery_app.conf.beat_schedule = {
    'check-file-every-10-seconds': {
        'task': 'app.tasks.check_file',
        'schedule': 10.0,
    },
}

celery_app.conf.timezone = 'UTC'
