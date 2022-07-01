from django.urls import path
from . import views


urlpatterns = [
    path('homepage/',views.homepage,name="post_home"),
    path('',views.list_post,name="list_post"),
    path('<int:post_index>/',views.post_detail,name='post_detail')
]