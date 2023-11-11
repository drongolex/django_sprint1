from django.shortcuts import render
from blog_mock import posts


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    context = {'post': posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
