from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['active']  = 'index'
        return context