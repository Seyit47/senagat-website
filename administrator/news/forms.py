from django import forms
from main.models import *

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'content', 'image',)