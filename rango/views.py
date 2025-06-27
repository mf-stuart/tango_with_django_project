from django.shortcuts import render, reverse
from django.http import HttpResponse

from tango_with_django_project import settings
from rango.models import Category, Page



# Create your views here.
def index(request):


    category_list = Category.objects.order_by('-likes')[:5]
    top_viewed_pages = Page.objects.order_by('-views')[:5]


    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                    'categories': category_list,
                    'pages': top_viewed_pages,}

    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict = {'category': category, 'pages': pages}
    except Category.DoesNotExist:
        context_dict = {'category': None, 'pages': None}

    return render(request, 'rango/category.html', context=context_dict)

def about(request):
    context_dict = {'boldtext': 'This tutorial has been put together by matthew', 'caturl': f'{settings.MEDIA_URL}cat.jpg' }
    return  render(request, 'rango/about.html', context=context_dict)