from django.contrib import admin

from .models import Book, Comment

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'book', 'recommended', 'is_active', 'datetime_created',)