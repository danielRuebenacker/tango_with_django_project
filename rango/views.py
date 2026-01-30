from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = { 'boldmessage': 'Watcha looking at? huh?' }
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says this is the about page! <a href='/rango/'>rango</a>")
