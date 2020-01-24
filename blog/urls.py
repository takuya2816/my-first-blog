from django.urls import path
from . import views

# URLのパターンが"views.post_list"の時
urlpatterns = [
    path('', views.post_list, name='post_list'),  # view作成とURLの名前
]

# post_listと言う名前のview