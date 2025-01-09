from django.contrib import admin

from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "image", "author", "created_at", "updated_at")
    list_display_links = ("author",)
    list_filter = ["created_at"]
