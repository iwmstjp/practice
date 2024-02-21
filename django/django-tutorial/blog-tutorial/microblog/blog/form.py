from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = ""
        fields = ["name", "email", "body"]