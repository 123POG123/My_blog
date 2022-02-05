from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    you_email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    query = forms.CharField()
