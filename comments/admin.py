from django.contrib import admin
from .models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','created_time']
    list_filter = ['name', 'email','created_time']

admin.site.register(Comment,CommentAdmin)
