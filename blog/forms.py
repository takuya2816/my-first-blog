from django import forms
from .models import Post

class PostForm(forms.ModelForm):  # フォームの名前

    class Meta:  # 
        model = Post  # モデルの指定
        fields = ('title', 'text',)  # titleとtextを伝える
