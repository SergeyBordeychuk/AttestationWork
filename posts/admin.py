from django.contrib import admin

from posts.models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image', 'owner')
    list_filter = ('created_at', )
    exclude = ()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    exclude = ()