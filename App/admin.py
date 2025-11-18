from django.contrib import admin
from .models import Article, Comment,Contact


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_time"]
    list_filter = ["created_time", "updated_time", "categories"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ["user_email","is_agree"]
    list_display = ["user_name", "user_email","is_agree"]


admin.site.register(Contact)