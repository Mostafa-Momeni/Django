from django import forms
from .models import Comments

class BlogPostCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            "name",
            "email",
            "address",
            "city",
            "province",
            "zip_code",
            "hide_name",
            "comment",
        ]