from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse

from tango_with_django_project import settings
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm



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

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('index'))
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'category': category, 'form': form}
    return render(request, 'rango/add_page.html', context=context_dict)

def about(request):
    context_dict = {'boldtext': 'This tutorial has been put together by matthew', 'caturl': f'{settings.MEDIA_URL}cat.jpg' }
    return  render(request, 'rango/about.html', context=context_dict)