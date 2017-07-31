from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
# 可以发现,这个forms文件的内容和之前慕课网的内容差很多,因为作用不一样.
# 慕课的例子,表单已经由前端写好了,所以只需要对特定数据做验证就好.
# 而这里,并没有表单,需要自己生成,所以使用Django自带功能就行.
