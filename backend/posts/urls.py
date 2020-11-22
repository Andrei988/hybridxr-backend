from django.urls import path
from .views import (
    post_list_view,
    apiOverview,
    post_detailed_view,
    contact_view,
    company_info_view
)

urlpatterns = [
    path('', apiOverview),
    path('post/list', post_list_view),
    path('post/<int:pk>', post_detailed_view),
    path('contact', contact_view),
    path('info', company_info_view),
]
