from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from posts.views import apiOverview, post_list_view, post_detailed_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', apiOverview),
    path('api/post/list', post_list_view),
    path('api/post/<int:pk>', post_detailed_view),
    path('api/contact', contact_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
