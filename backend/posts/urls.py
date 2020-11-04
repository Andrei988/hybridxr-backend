from django.urls import path
from .views import (
    post_list_view,
    post_create_view,
)

urlpatterns = [
    path('/posts', post_list_view),
    path('/create', post_create_view),
]
