from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 16)]
class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label="Количество")
    quantity = forms.IntegerField(initial=1, label="Количество", min_value=1, max_value=10)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
