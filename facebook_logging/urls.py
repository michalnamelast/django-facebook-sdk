from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('facebook-login/', views.facebook_login, name='facebook_login'),
    path('facebook-login-callback/', views.facebook_login_callback, name='facebook-login-callback'),
]