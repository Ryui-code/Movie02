from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='user')
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'actor', ActorViewSet, basename='actor')
router.register(r'movie_language', MovieLanguageViewSet, basename='movie-language')
router.register(r'rating', RatingViewSet, basename='rating')
router.register(r'favorite_movie', FavoriteMovieViewSet, basename='favorite-movie')
router.register(r'history', HistoryViewSet, basename='history')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls))
]