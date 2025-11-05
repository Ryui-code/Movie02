from modeltranslation.translator import TranslationOptions, register
from .models import Movie, Actor, Rating

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_description',)

class ActorTranslationOptions(TranslationOptions):
    fields = ('bio',)

class RatingTranslationOptions(TranslationOptions):
    fields = ('description',)