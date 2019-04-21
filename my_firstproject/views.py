"""from django.http import HttpResponse

def homepage(request):
    return HttpResponse('homepage')

def about(request):
    return HttpResponse('about')
"""
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
