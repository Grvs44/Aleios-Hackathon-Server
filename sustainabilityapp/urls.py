from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
import knox.views
from .views import *
from rest_framework.routers import DefaultRouter


app_name = 'sustainabilityapp'
router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'image', ImageViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/login/', LoginView.as_view(), name='knox_login'),
    path(r'auth/logout/', knox.views.LogoutView.as_view(), name='knox_logout'),
    path(r'auth/logoutall/', knox.views.LogoutAllView.as_view(),
         name='knox_logoutall'),
    path('auth/signup/', UserCreateAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
