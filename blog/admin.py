from csv import list_dialects
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment

# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class  PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)