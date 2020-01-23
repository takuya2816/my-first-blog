"""
アプリのロジックを書いていく
以前作ったモデルに情報を要求しテンプレートに渡す
"""

from django.shortcuts import render

# Create your views here.
# post_list関数の作成
#  テンプレートを（色々なものを合わせて）組み立てる render という関数
def post_list(request):
    return render(request, 'blog/post_list.html', {})