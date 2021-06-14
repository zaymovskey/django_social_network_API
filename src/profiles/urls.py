from django.urls import path, include
from .views import UserGetView, UsersListView, UserUpdateView, PostViewSet

urlpatterns = [
    path('users/all', UsersListView.as_view()),
    path('users/<int:pk>/', UserGetView.as_view()),
    path('users/update/', UserUpdateView.as_view()),

    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'list'})),
    path('posts/create/', PostViewSet.as_view({'post': 'create'})),
    path('posts/delete/<int:pk>/', PostViewSet.as_view({'delete': 'destroy'})),
    path('posts/like/<int:pk>/', PostViewSet.as_view({'post': 'like'})),

    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
]