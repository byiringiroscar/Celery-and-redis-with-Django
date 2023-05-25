from django.shortcuts import render, HttpResponse
from mainapp.tasks import test_func
from send_mail_app.tasks import send_main_function
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_main_function.delay()
    return HttpResponse('Sent')


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=11, minute=1)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"12", task='send_mail_app.tasks.send_main_function') #args=json.dumps(2,)
    return HttpResponse("Done again")