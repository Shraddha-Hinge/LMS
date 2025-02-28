from celery import shared_task
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_verification_email_task(user_id):
    try:
        user = User.objects.get(id=user_id)
        token = get_random_string(length=32)
        user.email_verification_token = token
        user.save()

        verification_link = f"http://localhost:8000/api/accounts/verify-email/{token}/"
        subject = "Verify Your Email"
        message = f"Click the link below to verify your email: {verification_link}"

        send_mail(subject, message, "noreply@lms.com", [user.email])
    except User.DoesNotExist:
        return "User not found"
