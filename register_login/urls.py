from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name = 'register_login_home'),
    path('logout', views.logout, name = 'register_login_logout'),
    path('register', views.register, name = 'register_login_register'),
    path('login', views.login, name = 'register_login_login'),
    path('user', views.load_account, name = 'register_login_loadAccount'),
]
