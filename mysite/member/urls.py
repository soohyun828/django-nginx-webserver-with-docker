from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('home/', views.home),
]
#회원가입 경로 http://127.0.0.1:8000/member/register
#로그인 경로 http://127.0.0.1:8000/member/login