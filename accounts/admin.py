from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'role', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('profile_picture',)}),
        ('Permissions', {'fields': ('is_active', 'role')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_active'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
