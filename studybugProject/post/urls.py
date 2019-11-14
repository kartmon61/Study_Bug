from django.urls import path
from .import views

urlpatterns = [
    #포스트 페이지
    path('post/',views.PostView.as_view(),name='list'),
    path('newpost/',views.PostCreate.as_view(),name='new'),
    path('detail/<int:pk>',views.PostDetail.as_view(),name='detail'),
    path('update/<int:pk>',views.PostUpdate.as_view(),name='change'),
    path('delete/<int:pk>',views.PostDelete.as_view(),name='del'),
    path('detail/commentcreate/<int:post_id>',views.commentcreate,name='commentcreate'),
    path('detail/commentdelete/<int:post_id>/<int:comment_id>',views.commentdelete,name='commentdelete'),
]