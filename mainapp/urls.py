from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name="test"),
    path('sendmail/', views.send_mail_to_all, name='send_mail_to_all'),
    path('schedulemail/', views.schedule_mail, name='schedule_mail')
]