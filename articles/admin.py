from django.contrib import admin
from .models import Article, Comment


# admin.StackedInline , either of these formats could be used based on ur preference
class CommentInline(admin.TabularInline):
    model = Comment
   # extra = 0  # change from default provided 3 empty rows to 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
