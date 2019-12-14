from django.urls import path

from . import views

urlpatterns = [
    path('set_role/', views.SetRoleView.as_view(), name='set_role'),
]