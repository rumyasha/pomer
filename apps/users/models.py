from django.contrib.auth.models import AbstractUser
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
    url = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    image_url = models.URLField(blank=True, null=True)

class CustomUser(AbstractUser):
        # Добавьте кастомные поля, если нужно
        phone = models.CharField(max_length=20, blank=True)

        class Meta:
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'

        def __str__(self):
            return self.email