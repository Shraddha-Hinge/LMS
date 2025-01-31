from django.contrib import admin
from .models import Batch, LiveSession

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_code')  
    search_fields = ('name',)  
    ordering = ('name',)  

@admin.register(LiveSession)
class LiveSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'batch', 'tutor', 'date', 'start_time', 'end_time', 'recording_link') 
    search_fields = ('title', 'batch__name', 'tutor__username')  
    list_filter = ('date', 'batch', 'tutor') 
    ordering = ('-date', 'start_time')  
    readonly_fields = ('recording_link',)  
