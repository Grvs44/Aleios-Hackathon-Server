from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


app_name = 'sustainabilityapp'
router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'post', PostViewSet)
router.register(r'image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('knox.urls')),
    path('auth/signup/', UserCreateAPIView.as_view()),
]
