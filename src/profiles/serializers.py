from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import CustomUser, Post, Like


class UserSerializer(serializers.ModelSerializer):
    """Вывод информации о пользователе"""

    class Meta:
        model = CustomUser
        exclude = ('password', 'last_login', 'is_staff', 'is_active', 'is_superuser')


class UserUpdateSerializer(serializers.ModelSerializer):
    """Обновление данных пользователя"""

    class Meta:
        model = CustomUser
        fields = ('status',)


class PostSerializer(serializers.ModelSerializer):
    """Пост"""
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'created_date', 'author', 'total_likes', 'liked')

    def get_liked(self, post):
        if 'user' in self.context:
            obj_type = ContentType.objects.get_for_model(post)
            like = Like.objects.filter(content_type=obj_type, object_id=post.id, user=self.context['user'])
            return like.exists()
        return False
