
from django import forms

from .models import *

class GatesForm(forms.ModelForm):

    class Meta:
        model = Gates
        fields = ('name', 'description', 'repost',)