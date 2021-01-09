from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import BlogPost, Category


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_post.html'