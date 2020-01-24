# リクエストを基にどのページを表示させるか決定する
# サーバーにアクセスされたらデータベースとテンプレートを動かす

"""
アプリのロジックを書いていく
以前作ったモデルに情報を要求しテンプレートに渡す
"""

from django.shortcuts import render
from .models import Post  #.は現在のディレクトリを示す
from django.utils import timezone

# requestを受け取りresponseを返す

def post_list(request):    
    # DB中のクエリセットの並び替え
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # requestを受けてrender関数でhtmlへクエリセットを組み合わせる
    return render(request, 'blog/post_list.html', {'posts': posts})  # {'名前':クエリセット}