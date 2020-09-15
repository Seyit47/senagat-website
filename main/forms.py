from django import forms
from django.forms import TextInput, EmailInput, Textarea, FileInput, DateTimeInput
from .models import *

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact_us
        fields = ('fullname', 'email', 'message',)
        widgets = {
            'fullname':TextInput(attrs={
                'placeholder':'Name, surname',
                'class':'base-input',
            }),
            'email':EmailInput(attrs={
                'placeholder':'E-mail address',
                'class':'base-input'
            }),
            'message':Textarea(attrs={
                'placeholder':'Your letter',
                'rows':'8',
                'class':'base-input',
                'cols':'',
                'style':'color: #fff'
            })
        }