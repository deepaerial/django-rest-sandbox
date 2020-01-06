from django.urls import path
from rest_framework import routers

from api.endpoints.auth import views as auth_views

router = routers.SimpleRouter()

urlpatterns = [
    path(
        'auth/login/',
        auth_views.LoginAPIView.as_view(),
        name='auth.login'
    ),
    path(
        'auth/logout/',
        auth_views.LogoutAPIView.as_view(),
        name='auth.logout'
    ),
]
