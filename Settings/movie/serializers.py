from rest_framework import serializers
from tokenize import TokenError
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            'status',
            'data_registered',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = CustomUser.objects.create_user(**validate_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {'username': instance.username,
                     'email': instance.email,
                },
            'access': str(refresh.access_token),
                'refresh': str(refresh)
            }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = CustomUser.objects.filter(username=username).first()
        if not user:
            raise serializers.ValidationError('No user found with this username')
        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError('Incorrect credentials')
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }

class LogoutSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField(required=True)

    def validate(self, data):
        refresh_token = data.get('refresh')
        try:
            token = RefreshToken(refresh_token)
            return token
        except TokenError:
            raise serializers.ValidationError({'detail': 'No token like this'})

    def save(self):
        refresh_token = self.validated_data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class SimpleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountrySerializer(many=True)
    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_image', 'country', 'date', 'movie_status']

class MovieLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguage
        fields = ['language', 'video']

class RatingSerializer(serializers.ModelSerializer):
    user = SimpleProfileSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Rating
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'