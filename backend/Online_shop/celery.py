import os
from celery import Celery

# Ustawienie domyślnego modułu ustawien Django dla 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Online_shop.settings')

app = Celery('Online_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()