from django.contrib import admin
from .models import  Article
from ..news.models import Source, Category


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'published_at', 'is_published')
    list_filter = ('source', 'categories', 'is_published')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_at'
    filter_horizontal = ('categories',)