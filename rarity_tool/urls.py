from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('kings_tom', views.kings_tom, name='kings_tom'),
    #------------ First ----------------------
    path('rarity_tool', views.rarity_tool, name='rarity_tool'),
    path('first_url', views.first_url, name='first_url'),
    path('des_rarity_tool', views.des_rarity_tool, name='des_rarity_tool'),
    path('des_first_url', views.des_first_url, name='des_first_url'),
    path('filter', views.filter, name='filter'),
    path('filter_url', views.filter_url, name='filter_url'),
    #------------ All ----------------------
    path('all_rarity_tool', views.all_rarity_tool, name='all_rarity_tool'),
    path('all_url', views.all_url, name='all_url'),
    path('des_all_rarity_tool', views.des_all_rarity_tool, name='des_all_rarity_tool'),
    path('des_all_url', views.des_all_url, name='des_all_url'),
    path('filter_all', views.filter_all, name='filter_all'),
    path('filter_url_all', views.filter_url_all, name='filter_url_all'),
    #------------ Secondary ----------------------
    path('secondary_rarity_tool', views.secondary_rarity_tool, name='secondary_rarity_tool'),
    path('second_url', views.second_url, name='second_url'),
    path('des_secondary_rarity_tool', views.des_secondary_rarity_tool, name='des_secondary_rarity_tool'),
    path('des_secondary_url', views.des_secondary_url, name='des_secondary_url'),
    path('secondary_filter', views.secondary_filter, name='secondary_filter'),
    path('secondary_filter_url', views.secondary_filter_url, name='secondary_filter_url'),
    
]