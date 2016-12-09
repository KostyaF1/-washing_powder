# -*- coding: utf-8 -*- 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from products.models import Powder


class PowderListView(ListView):
    model = Powder
    
    def get_queryset(self):
        products = Powder.objects.all()
        return products

class PowderDetailView(DetailView):
    model = Powder
    template_name = 'products/detail.html'
    context_object_name = 'powder'
    
    def get_context_data(self, **kwargs):
        context = super(PowderDetailView, self).get_context_data(**kwargs)
        #context['options'] = Option.objects.filter(service = self.object)
        return context
