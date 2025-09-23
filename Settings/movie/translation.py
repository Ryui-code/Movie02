from modeltranslation.translator import TranslationOptions, register
from .models import Movie, Actor, Country

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'actor_bio')

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'movie_description')