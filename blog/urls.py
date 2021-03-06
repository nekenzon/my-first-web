from django.urls import path
from . import views
from django.urls import re_path
from django.conf.urls import url, include


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/edit1/', views.post_edit_superuser, name='post_edit1'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('index', views.index, name='index'),
    path('post_list', views.post_list, name='post_list'),
    path('pics', views.album, name='album'),
    path('about', views.about, name='about'),
    path('login_user',views.login_user,name='login_user'),
    path('post_register', views.post_register, name='post_register'),
    path('simple_upload',views.simple_upload2,name='simple_upload'),
    path('post/<int:pk>/edit/simple_upload/', views.simple_upload,name='simple_upload2'),
    path('post_search',views.searchposts,name='post_search'),
    path('pics/<int:pk>/dele',views.dele,name='dele'),
    path('cv', views.cv, name='cv'),
    path('error', views.error, name='error'),
    path('admin_login',views.admin,name='admin'),
]
