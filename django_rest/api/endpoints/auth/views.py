from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import login, logout
from api.base import BaseApiView

from .serializers import LoginSerializer, UserSerializer


class LoginAPIView(BaseApiView):
    """
    REST API login endpoint
    """
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response(UserSerializer(user).data)


class LogoutAPIView(BaseApiView):
    """
    REST API logout endpoint
    """

    permission_classes = [permissions.IsAuthenticated]    

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'OK'})
