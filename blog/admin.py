from django.contrib import admin

from .models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'active']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'active']
