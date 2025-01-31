from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Batch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color_code = models.CharField(max_length=7, help_text="Hex color code for calendar events")

    def __str__(self):
        return self.name


class LiveSession(models.Model):
    title = models.CharField(max_length=200)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="sessions")
    tutor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="live_sessions")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    meeting_link = models.URLField()
    recording_file = models.FileField(upload_to="live_sessions/recordings/", blank=True, null=True, help_text="Upload session recording file")
    recording_link = models.URLField(blank=True, null=True, help_text="Link to session recording")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.date})"


# Signal to send email reminders for upcoming sessions
@receiver(post_save, sender=LiveSession)
def send_session_reminder(sender, instance, created, **kwargs):
    if created:
        # Here, we send a reminder email 24 hours before the session date
        reminder_time = timezone.make_aware(timezone.datetime.combine(instance.date, instance.start_time)) - timezone.timedelta(days=1)
        
        # Logic to check if it's time to send a reminder
        if timezone.now() >= reminder_time:
            subject = f"Reminder: Upcoming Session - {instance.title}"
            message = f"Dear {instance.tutor.username},\n\nThis is a reminder about your upcoming session on {instance.date} at {instance.start_time}.\n\nSession: {instance.title}\nMeeting Link: {instance.meeting_link}"
            recipient_list = [instance.tutor.email] if instance.tutor else []
            
            send_mail(subject, message, 'admin@example.com', recipient_list)
