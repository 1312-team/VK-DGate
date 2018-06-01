
from django import forms

from .models import *

class GatesForm(forms.ModelForm):

    class Meta:
        model = Gate
        fields = ('name', 'description', 'link', 'repost',)