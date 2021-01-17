from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category', 'author')
    list_display = ('id', 'title', 'author', 'published', 'mvp', 'featured')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'author', 'category')
    list_editable = ('mvp', 'featured')
    list_filter = ('category', 'featured')
    list_per_page = 25


admin.site.register(Blog, BlogAdmin)
