from django.contrib import admin
from .models import Message  # Corrected 'model' to 'models'
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'score']
    
admin.site.register(Message, MessageAdmin)  # Corrected 'Messasage' to 'Message'
