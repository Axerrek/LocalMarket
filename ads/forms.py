from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ["title", "description", "price", "region", "category", "image"]

class AdFilterForm(forms.Form):
    category = forms.ChoiceField(required=False)
    price_min = forms.IntegerField(required=False)
    price_max = forms.IntegerField(required=False)
    region = forms.CharField(required=False)