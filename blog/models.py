# Create your models here.
# ブログポストモデルの定義、
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # objectの状態定義
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 著者
    title = models.CharField(max_length=200)  # タイトル
    text = models.TextField()  # 本文
    created_date = models.DateTimeField(default=timezone.now)  # 作成日
    published_date = models.DateTimeField(blank=True, null=True)  # 出稿日

    def publish(self):
        self.published_date = timezone.now()  # 現在時刻の取得
        self.save()

    def __str__(self):
        return self.title