from django.http import HttpResponse

from .models import CustomUser, Post
from .serializers import UserSerializer, UsersListSerializer, UserUpdateSerializer, PostsListSerializer, \
    PostCreateSerializer, PostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UserGetView(generics.RetrieveAPIView):
    """Вывод данных одного опользователя"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UsersListView(generics.ListAPIView):
    """Вывод списка всех пользователей"""
    queryset = CustomUser.objects.all()
    serializer_class = UsersListSerializer


class UserUpdateView(generics.UpdateAPIView):
    """Обновление данных авторизованного пользователя"""
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return CustomUser.objects.get(auth_token=self.request.auth)


class PostsListView(generics.ListAPIView):
    """Вывод всех постов пользователя"""
    queryset = CustomUser.objects.all()
    serializer_class = PostsListSerializer

    def get_queryset(self):
        return Post.objects.filter(author__id=self.kwargs['pk'])


class PostCreateView(generics.CreateAPIView):
    """Создание поста"""
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        if CustomUser.objects.get(auth_token=self.request.auth) != CustomUser.objects.get(posts__id=self.kwargs['pk']):
            return HttpResponse('Нет доступа', status=401)
        return super(PostDeleteView, self).destroy(self, request, *args, **kwargs)
