from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter

from django.contrib.auth.models import User
from .serializers import MovieSerializer, UserSerializer, ModelSerializer, MovieDescriptionSerializer
from .models import Movie, MovieDescription
from .paginations import CustomPagination
# Create your views here.


class UserViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [permissions.IsAuthenticated, ]

    # def get_queryset(self):
    #     user = User.objects.all()
    #     return user


class MovieViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name']
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [permissions.IsAuthenticated, ]


class MovieDescriptionViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = MovieDescription.objects.all()
    serializer_class = MovieDescriptionSerializer
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter, SearchFilter]
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [permissions.IsAuthenticated, ]
