from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html')


def index(request):
    return render(request, 'pages/index.html')
