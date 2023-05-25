from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery_with_django import settings


from celery import shared_task


@shared_task(bind=True)
def send_main_function(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "we are testing celery please don't worry oscar it's only testing again hhh"
        to_email = user.email
        send_mail(
            subject=mail_subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[to_email],
            fail_silently=False
        )

    return "Done"
