from django.db import models

from users.models import User


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=150, verbose_name='заголовок поста')
    text = models.TextField(verbose_name='текст поста')
    image = models.ImageField(blank=True, null=True, verbose_name='изображение', upload_to='articles/image/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор поста')
    #comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.name} - {self.author}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор комментария')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='ссылка на пост')
    text = models.TextField(verbose_name='текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.post} - {self.author} - {self.created_at}"
