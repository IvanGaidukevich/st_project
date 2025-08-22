from django.contrib import admin
from blog.models import Post, Comment, PostStatus


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostStatus)
class PostStatusAdmin(admin.ModelAdmin):
    pass
