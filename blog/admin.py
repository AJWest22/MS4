from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'created',
        'updated',
        'title',
        'posts',
    )


admin.site.register(Blog, BlogAdmin)
