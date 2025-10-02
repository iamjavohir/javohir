from django.contrib import admin
from .models import Post, PostContent


class PostContentInline(admin.TabularInline):
    model = PostContent
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostContentInline]