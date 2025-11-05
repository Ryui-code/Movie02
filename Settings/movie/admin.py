from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password', 'email', 'status', 'data_registered', 'token'
            ),
        }),
    ]
    readonly_fields = ['token', 'data_registered']

class MovieLanguageInline(admin.TabularInline):
    model = MovieLanguage
    extra = 3

admin.register(Movie)
class Admin(TranslationAdmin):
    inlines = [MovieLanguageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.register(Actor)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Rating)
admin.site.register(FavoriteMovie)
admin.site.register(History)