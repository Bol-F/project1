from django.conf import settings
from django.core.mail import send_mail, EmailMessage
import threading


def send_email(subject, message, to_email):
    send_mail(subject=subject,
              message=message,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[to_email],
              fail_silently=True,
              )


def send_email_thread(subject, message, to_email):
    thread = threading.Thread(target=send_email, args=(subject, message, to_email))
    thread.start()


def send_email_with_thread():
    t = threading.Thread(target=send_email_with_file)
    t.start()


def send_email_with_file():
    email = EmailMessage(
        subject='test',
        body='test',
        from_email=settings.EMAIL_HOST_USER,
        to=['bolievfirdavs0@gmail.com']
    )
    email.attach_file('')
    email.send()
