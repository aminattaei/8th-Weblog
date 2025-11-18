from django import forms
from .models import Article, Comment,Contact    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("user_name", "user_email", "user_comment")


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("full_name",'email','message')
