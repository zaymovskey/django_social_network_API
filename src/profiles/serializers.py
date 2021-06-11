from rest_framework import serializers
from .models import CustomUser, Post


class UserSerializer(serializers.ModelSerializer):
    """Вывод информации о пользователе"""

    class Meta:
        model = CustomUser
        exclude = ('password', 'last_login', 'is_staff', 'is_active', 'is_superuser')


class UsersListSerializer(serializers.ModelSerializer):
    """Список всех пользователей"""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'birthday', 'avatar', 'bio', 'first_name', 'last_name')


class UserUpdateSerializer(serializers.ModelSerializer):
    """Обновление данных пользователя"""

    class Meta:
        model = CustomUser
        fields = ('status',)


class PostsListSerializer(serializers.ModelSerializer):
    """Список постов"""

    class Meta:
        model = Post
        fields = ('id', 'text', 'created_date')


class PostCreateSerializer(serializers.ModelSerializer):
    """Создание поста"""

    class Meta:
        model = Post
        fields = ('id', 'text', 'created_date', 'author')


class PostSerializer(serializers.ModelSerializer):
    """Пост"""
    class Meta:
        model = Post
        fields = '__all__'
