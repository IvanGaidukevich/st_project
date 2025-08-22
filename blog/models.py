from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PostStatus(models.Model):
    name = models.CharField(max_length=16, verbose_name='Статус', unique=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    body = models.TextField(verbose_name="Основная часть")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    status = models.ForeignKey(PostStatus, on_delete=models.CASCADE, verbose_name="Статус")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Слаг")

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    body = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.author.username} на {self.post}'

