from django import forms

from blog.models import Comment

from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
    def __init__(self):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        
    class Meta:
        model = Comment
        fields = ["content"]
