from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('first_rarity_tools', views.first_rarity_tools, name='first_rarity_tools'),
    path('first_url', views.first_url, name='first_url'),
    path('price', views.price, name='price'),
    path('price_url', views.price_url, name='price_url'),
    path('rank', views.rank, name='rank'),
    path('rank_url', views.rank_url, name='rank_url'),
    path('index_url', views.index_url, name='index_url'),
    path('get_data', views.get_data, name='get_data'),
]