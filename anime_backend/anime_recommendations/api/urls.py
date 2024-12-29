from django.urls import path
from .views import anime_recommendation
from .views import get_anime_list

urlpatterns = [
    path('anime-list', get_anime_list, name='get_anime_list'),
]
