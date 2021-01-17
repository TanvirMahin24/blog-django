from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category', 'author')
    list_display = ('id', 'name', 'author', 'published', 'mvp', 'featured')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'author', 'category')
    list_editable = ('mvp', 'featured')
    list_filter = ('category', 'featured')
    list_per_page = 25


admin.site.register(BlogAdmin, Blog)
