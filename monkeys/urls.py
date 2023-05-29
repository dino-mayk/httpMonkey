from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.list,
        name='list',
    ),
    path(
        '<int:pk>/',
        views.detail,
        name='detail',
    ),
]
