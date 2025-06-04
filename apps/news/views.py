from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from django.utils import timezone
from rest_framework.permissions import AllowAny


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API для просмотра новостей.
    Фильтры:
    - ?published=true - только опубликованные
    - ?category=slug - по категории
    - ?source=id - по источнику
    """
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Article.objects.all()

        # Фильтр по статусу публикации
        if self.request.query_params.get('published') == 'true':
            queryset = queryset.filter(is_published=True)

        # Фильтр по категории
        category_slug = self.request.query_params.get('category')
        if category_slug:
            queryset = queryset.filter(categories__slug=category_slug)

        # Фильтр по источнику
        source_id = self.request.query_params.get('source')
        if source_id:
            queryset = queryset.filter(source_id=source_id)

        return queryset.order_by('-published_at')