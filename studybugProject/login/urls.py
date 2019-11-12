from django.urls import path
from .import views

urlpatterns = [
    #메인 페이지
    path('',views.loading,name='loading'),
    path('login',views.login,name='login'),
]