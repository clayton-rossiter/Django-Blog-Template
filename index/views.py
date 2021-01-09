from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'