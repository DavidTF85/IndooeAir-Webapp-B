
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('instruments/create', views.Instruments_create_page, name='Instruments_create_page'),
    path('instrument/list', views.Instruments_lists_page, name='Instruments_lists_page'),
    path('instrument/retrieve', views.i_retrieve_page, name='i_retrieve_page'),
    path('instrument/update', views.Instruments_update_page, name='Instruments_update_page'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
