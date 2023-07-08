from django.urls import path

from api import views

urlpatterns = [
    path(
        '<int:pk>/',
        views.detail,
        name='detail'
    ),
]
