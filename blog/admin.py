from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'created',
        'updated',
        'title',
        'post',
        'image',
    )


admin.site.register(Post, PostAdmin)
