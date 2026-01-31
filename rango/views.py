from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from rango.models import Category
from rango.models import Page

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!' 
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = { 'boldmessage': 'This tutorial has been put together by Daniel.', } 
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
