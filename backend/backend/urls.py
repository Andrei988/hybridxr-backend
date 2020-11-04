from django.urls import path, include
from django.contrib import admin
from django.urls import path

from posts.views import apiOverview, post_list_view, post_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', apiOverview),
    path('api/post/list', post_list_view),
    path('api/post/create', post_create_view),
]
