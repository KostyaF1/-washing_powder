# -*- coding: utf-8 -*- 
from django import forms
from feedbacks.models import Feedback, CallOrder

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

class CallOrderForm(forms.ModelForm):
    class Meta:
        model = CallOrder
        fields = '__all__'
