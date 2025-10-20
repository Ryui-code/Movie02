from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'register', ProfileViewSet, basename='user')
router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'movie_languages', MovieLanguageViewSet, basename='movie-language')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'favorites', FavoriteViewSet, basename='favorites')
router.register(r'favorite_movies', FavoriteMovieViewSet, basename='favorite-movie')
router.register(r'histories', HistoryViewSet, basename='history')

urlpatterns = [
    path('register/', CustomUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]