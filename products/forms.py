# -*- coding: utf-8 -*- 
from django import forms
from products.models import Powder, PowderOrder


class PowderOrderForm(forms.ModelForm):
    class Meta:
        model = PowderOrder
        fields = '__all__'
        data = {'name': Powder}
        form = PowderOrder(data)
