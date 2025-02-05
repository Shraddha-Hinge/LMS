from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

