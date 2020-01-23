from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # view作成とURLの名前
]
