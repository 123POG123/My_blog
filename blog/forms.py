from django import forms
from django.contrib.auth.models import User

from blog.models import Comment


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ('username', 'first_name', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('упс пароли не совпадают.')
        return cd['password2']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    you_email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    query = forms.CharField()
