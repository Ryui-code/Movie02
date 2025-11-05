from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import DateField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('Guest', 'Guest'),
    ('Author', 'Author')
)

class CustomUser(AbstractUser):
    status = models.CharField(choices=STATUS_CHOICES, default='Guest')
    data_registered = DateField(auto_now_add=True)
    token = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.username

class Actor(models.Model):
    full_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])
    phone_number = PhoneNumberField(null=True, blank=True)
    bio = models.TextField()
    image = models.ImageField()

class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    movie_date = DateField()
    movie_country = CountryField(default='Kyrgyzstan')
    movie_actor = models.ManyToManyField(Actor, related_name='actors')
    TYPES_CHOICES = (
    ('144p', '144p'),
    ('270p', '270p'),
    ('360p', '360p'),
    ('480p', '480p'),
    ('720p', '720p'),
    ('1080p', '1080p'),
    )
    types = models.CharField(choices=TYPES_CHOICES, default='480')
    movie_time = models.DurationField()
    movie_description = models.TextField()
    movie_trailer = models.URLField()
    movie_image = models.ImageField()

    def __str__(self):
        return self.movie_name

    def rating(self):
        rate = self.ratings.all()
        if rate.exists():
            return round(sum([i.stars for i in rate]) / rate.count(), 2)
        return 'No ratings'

class MovieLanguage(models.Model):
    language = models.CharField(max_length=64)
    video = models.FileField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return f'{self.movie} - {self.language}'

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie

class FavoriteMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie

class History(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie