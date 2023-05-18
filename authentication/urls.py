from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout')
]