from django import forms
from .models import *

class Subscriberform(forms.ModelForm):
    class Meta:
        model = subscriber
        exclude = ["replied", "reply",]
