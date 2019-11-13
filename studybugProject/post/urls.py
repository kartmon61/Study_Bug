from django.urls import path
from .import views

urlpatterns = [
    #포스트 페이지
    path('post/',views.post,name='post'),
]