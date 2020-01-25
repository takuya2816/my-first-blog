from django.urls import path
from . import views

# URLのパターンが"views.post_list"の時
urlpatterns = [
    path('', views.post_list, name='post_list'),  # view作成とURLの名前
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),  # post/new/というURLがある時, views.post_new,を実行し、name='post_new'をURLに追加
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # edit
]  # <int:pk>にはpkの数字が入る

# post_listと言う名前のview