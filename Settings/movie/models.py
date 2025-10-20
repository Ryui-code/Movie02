from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple')
)

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(12), MaxValueValidator(75)], null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='simple')
    data_registered = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

class Actor(models.Model):
    actor_name = models.CharField(max_length=64)
    actor_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(25)])
    actor_bio = models.TextField()
    actor_image = models.ImageField()

class Country(models.Model):
    country_name = models.CharField(max_length=64)

    def __str__(self):
        return self.country_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    movie_date = DateTimeField()
    movie_country = models.ManyToManyField(Country, related_name='countries')
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
    movie_status = models.CharField(choices=STATUS_CHOICES, default='simple')

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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.movie}'

class Favorite(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class FavoriteMovie(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.favorite} - {self.movie}'

class History(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user