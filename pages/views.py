from django.shortcuts import render
from blogs.models import Blog


def about(request):
    return render(request, 'pages/about.html')


def index(request):
    blogs = Blog.objects.order_by('-blog_created').filter(published=True)
    mvp = Blog.objects.all().filter(mvp=True)
    blog_list = Blog.objects.order_by(
        '-blog_created').filter(published=True)[0:3]
    active_blog_id = blog_list[0].id

    context = {
        'blogs': blogs,
        'mvp_blog': mvp,
        'blog_list': blog_list,
        'active_blog_id': active_blog_id
    }
    return render(request, 'pages/index.html', context)
