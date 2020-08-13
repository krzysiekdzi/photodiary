from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(label="author", max_length=30)
    text = forms.CharField(label='text', max_length=100)