from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .filter import MovieFilter
from .permissions import GuestRestrictedPermission
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = JsonResponse({'detail': 'Successfully registered.'})
        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        return response

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        response = JsonResponse({'detail': 'Successfully logged in.'})

        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        return response

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = JsonResponse({'detail': 'Successfully logged out.'})
        response.delete_cookie('auth_token')
        return response

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [GuestRestrictedPermission]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [GuestRestrictedPermission]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['movie_name']
    ordering_fields = ['movie_date', 'movie_time']
    filterset_class = MovieFilter
    permission_classes = [GuestRestrictedPermission]

class MovieLanguageViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguage.objects.all()
    serializer_class = MovieLanguageSerializer
    permission_classes = [GuestRestrictedPermission]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [GuestRestrictedPermission]

class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer
    permission_classes = [GuestRestrictedPermission]

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [GuestRestrictedPermission]