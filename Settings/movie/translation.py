from modeltranslation.translator import TranslationOptions, register
from .models import Movie, Actor, Rating

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_description',)

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('bio',)

register(Rating)
class RatingTranslationOptions(TranslationOptions):
    fields = ('description',)