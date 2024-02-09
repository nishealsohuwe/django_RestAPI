from rest_framework.authtoken.views import obtain_auth_token

from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', views.signup),
    path('employees/', views.employees, name="employees"),
    path('api/', include(router.urls)),
    path('api-token-auth//', obtain_auth_token, name='api-token-auth/'),
]
