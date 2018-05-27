from django import forms
# from uploads.core.models import Document
from .models import *

class pc_form(forms.ModelForm):
    class Meta:
        model = Product_comments
        exclude = ["pc_created", "pc_updated", 'pc_reply','pc_replied', "pc_product",]
