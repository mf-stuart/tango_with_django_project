import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure and add the data to our models.

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 25},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 67},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 2}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 65},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com',
         'views': 17},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 12}
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 23},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 30}
    ]

    cats = {'Python': {'views': 128, 'likes': 64,'pages': python_pages,},
            'Django': {'views': 64, 'likes': 32,'pages': django_pages,},
            'Other Frameworks': {'views': 32, 'likes': 16,'pages': other_pages,}
            }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

    add_superuser()

def add_superuser():
    if not User.objects.filter(username='mf-stuart').exists():
        superuser = User.objects.create_superuser('mf-stuart', 'mf-stuart@outlook.com', 'djangorules')
        superuser.save()

def add_cat(name, views=0, likes=0):
    cat = Category.objects.get_or_create(
        name=name,
        views=views,
        likes=likes
    )[0]
    cat.save()
    return cat

def add_page(cat, title, url, views=0):
    page = Page.objects.get_or_create(
        category=cat,
        title=title,
        url=url,
        views=views,
    )[0]
    page.save()
    return page

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()