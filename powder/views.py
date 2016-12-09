# -*- coding: utf-8 -*- 
from django.views.generic import TemplateView
from products.models import Powder, AboutPowder, NavButton, Contact


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['powder'] = Powder.objects.all()
        context['about_powder'] = AboutPowder.objects.all()
        context['nav_buttons1'] = NavButton.objects.get(number=1)
        context['nav_buttons2'] = NavButton.objects.get(number=2)
        context['nav_buttons3'] = NavButton.objects.get(number=3)
        context['nav_buttons4'] = NavButton.objects.get(number=4)
        context['nav_buttons5'] = NavButton.objects.get(number=5)
        context['contacts'] = Contact.objects.all()
        context['email_us'] = NavButton.objects.get(number=5)
        return context
