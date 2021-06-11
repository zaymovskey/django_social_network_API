from django.urls import path, include
from .views import UserGetView, UsersListView, UserUpdateView, PostsListView, PostCreateView, PostDeleteView

urlpatterns = [
    path('users/all', UsersListView.as_view()),
    path('users/<int:pk>/', UserGetView.as_view()),
    path('users/update/', UserUpdateView.as_view()),

    path('posts/<int:pk>/', PostsListView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view()),

    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
]