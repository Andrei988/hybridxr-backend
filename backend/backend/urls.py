from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls'))
]
print("--------------------------------------------------------------")
print(settings.MEDIA_URL)
print(settings.MEDIA_ROOT)
print("--------------------------------------------------------------")
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
