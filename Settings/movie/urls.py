from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'register', ProfileViewSet, basename='users')
router.register(r'actor', ActorViewSet, basename='actors')
router.register(r'movie_language', MovieLanguageViewSet, basename='movie-languages')
router.register(r'rating', RatingViewSet, basename='ratings')
router.register(r'favorite', FavoriteViewSet, basename='favorites')
router.register(r'favorite_movie', FavoriteMovieViewSet, basename='favorite-movies')
router.register(r'history', HistoryViewSet, basename='histories')

urlpatterns = [
    path('', include(router.urls))
]