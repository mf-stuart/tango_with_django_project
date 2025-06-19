from django.shortcuts import render, reverse
from django.http import HttpResponse

from tango_with_django_project import settings


# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldtext': 'This tutorial has been put together by matthew', 'caturl': f'{settings.MEDIA_URL}cat.jpg' }
    return  render(request, 'rango/about.html', context=context_dict)