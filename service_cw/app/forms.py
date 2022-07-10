from django import forms

class OrderForm(forms.Form):
    address = forms.CharField()
    tel = forms.IntegerField()