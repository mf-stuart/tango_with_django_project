from django.urls import path
from . import views

app_name = 'rango'  # helps with namespacing

urlpatterns = [
    # Example route:
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
