from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('add_from_file', views.add_from_file, name='add_from_file'),
]
