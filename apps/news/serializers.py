from rest_framework import serializers
from .models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    source = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'source',
            'categories',
            'url',
            'published_at',
            'image_url',
            'is_published'
        ]