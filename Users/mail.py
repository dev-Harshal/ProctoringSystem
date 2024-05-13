from django.core.mail import send_mail
from django.conf import settings


def send_mail_to_the_user(recipient,otp):
    subject = f'Proctoring.AI'
    message = f'Your OTP for Proctoring.AI is {otp}'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [recipient])