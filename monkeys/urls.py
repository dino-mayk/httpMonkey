from django.urls import path
from monkeys import views

app_name = 'monkeys'

urlpatterns = [
    path(
        '',
        views.list,
        name='list',
    ),
    path(
        'status/<int:pk>/',
        views.detail,
        name='detail',
    ),
]
