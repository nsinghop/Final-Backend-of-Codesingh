# Celery configuration for Django
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edtech.settings')

app = Celery('edtech')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
