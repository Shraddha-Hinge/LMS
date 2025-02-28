from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'role', 'is_active', 'is_email_verified')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('profile_picture',)}),
        ('Permissions', {'fields': ('is_active', 'is_email_verified', 'role')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, CustomUserAdmin)
