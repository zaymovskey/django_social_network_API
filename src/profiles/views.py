from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CustomUser, Post, Like
from .serializers import UserSerializer, UserUpdateSerializer, PostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserGetView(generics.RetrieveAPIView):
    """Вывод данных одного опользователя"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UsersListView(generics.ListAPIView):
    """Вывод списка всех пользователей"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    """Обновление данных авторизованного пользователя"""
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return CustomUser.objects.get(auth_token=self.request.auth)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def destroy(self, request, *args, **kwargs):
        if CustomUser.objects.get(auth_token=self.request.auth) != CustomUser.objects.get(posts__id=self.kwargs['pk']):
            return HttpResponse('Нет доступа', status=401)
        super(PostViewSet, self).destroy(self, request, *args, **kwargs)
        return Response()

    def list(self, request, *args, **kwargs):
        queryset = Post.objects.filter(author__id=kwargs['pk'])
        if self.request.auth:
            user = CustomUser.objects.get(auth_token=self.request.auth)
            serializer = PostSerializer(queryset, many=True, context={'user': user})
            return Response(serializer.data)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def like(self, request, *args, **kwargs):
        user = CustomUser.objects.get(auth_token=self.request.auth)
        post = Post.objects.get(pk=kwargs['pk'])
        obj_type = ContentType.objects.get_for_model(post)
        obj, created = Like.objects.get_or_create(content_type=obj_type, object_id=post.id, user=user)
        if created:
            obj.save()
            return Response(data=True)
        obj.delete()
        return Response(data=False)
