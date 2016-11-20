from django.contrib import admin

from .models import Spam

class SpamAdmin(admin.ModelAdmin):
	list_display = ['text', 'published_date', 'user']

admin.site.register(Spam, SpamAdmin)
