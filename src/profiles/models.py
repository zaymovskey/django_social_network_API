from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class CustomUser(AbstractUser):
    """Кастомизированный пользователь"""

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')


class Like(models.Model):
    """Лайк"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Лайки', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return 'Лайк пользователя - {}'.format(self.user.username)


class Post(models.Model):
    """Пост"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор',
                               related_name='posts')
    text = models.TextField('Текст')
    created_date = models.DateTimeField('Создано', auto_now_add=True)
    likes = GenericRelation(Like, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return 'Пост пользователя - {}'.format(self.author.username)

    def total_likes(self):
        return self.likes.count()
