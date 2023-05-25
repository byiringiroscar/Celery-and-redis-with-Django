from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
import sys
from celery._state import _set_current_app
import django
from django.conf import settings



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_with_django.settings')
app = Celery('celery_with_django',)
app.conf.enable_utc = False
app.conf.update(timezone='Africa/Kigali')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
_set_current_app(app)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../celery_with_django')))
django.setup()
# celery beat settings
app.conf.beat_schedule = {
    'send-mail-every-at-8': {
        'task': 'send_mail_app.tasks.send_main_function',
        'schedule': crontab(hour=12, minute=10),
        # 'args': (2)
    }

}

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')