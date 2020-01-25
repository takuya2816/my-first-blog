# リクエストを基にどのページを表示させるか決定する（ページ遷移）
# サーバーにアクセスされたらデータベースとテンプレートを動かす

"""
アプリのロジックを書いていく
以前作ったモデルに情報を要求しテンプレートに渡す
"""

from django.shortcuts import render
from .models import Post  #.は現在のディレクトリを示す
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# requestを受け取りresponseを返す

def post_list(request):    
    # DB中のクエリセットの並び替え
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # requestを受けてrender関数でhtmlへクエリセットを組み合わせる
    return render(request, 'blog/post_list.html', {'posts': posts})  # {'名前':クエリセット}


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # pkにkeyが入っていない時PageNotFoundPageに飛ぶ
    # post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    # フォームの保存を可能にする
    print("post_new")

    if request.method == "POST":  # フォームにデータ入力がされている場合
        form = PostForm(request.POST)
        print("SAVE")

        # フォームに有効な値が入っているかどうか
        if form.is_valid():
            post = form.save(commit=False)  # ???フォームをまだ保存していないことを示す
            post.author = request.user  # 著者
            post.published_date = timezone.now()  # 投稿時間
            post.save()  #保存
            return redirect('post_detail', pk=post.pk)  # リダイレクトでpost_detailに遷移
    else:  # 最初にページにアクセスした時
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):  # editモード
    post = get_object_or_404(Post, pk=pk)  # オブジェクトが含まれていない場合はエラー画面に遷移
    if request.method == "POST":  # フォームに値が含まれる場合
        form = PostForm(request.POST, instance=post)  #indtanceには指定したpostモデルが入る
        if form.is_valid():  # 有効な値が含まれるかどうか
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:  # 最初にページにアクセスしたとき
        form = PostForm(instance=post)  # 編集フォームを開く
    return render(request, 'blog/post_edit.html', {'form': form})
