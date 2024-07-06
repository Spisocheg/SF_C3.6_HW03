from django.urls import path, include
from .views import PostsList, PostDetail

urlpatterns = [
    path('', PostsList.as_view(), name='list'),
    path('<int:pk>', PostDetail.as_view(), name='detail')
]
