

# Register your models here.
from django.contrib import admin
from .models import Admin

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'is_superuser']
