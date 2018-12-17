from django import forms

from .models import Advertise

class PostForm(forms.ModelForm):

    class Meta:
        model = Advertise
        fields = ('title', 'text',)