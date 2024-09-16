from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name='index'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/',views.register,name='register'),
    path('member/', views.member, name='member'),
    path('member/details/<int:id>', views.details, name='details'),
    path('profile/<int:id>', views.profile, name='profile'),
    # path('member/details/<slug:slug>', views.details, name='details'),
]

