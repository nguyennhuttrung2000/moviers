from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet, "user")
router.register("movies", views.MovieViewSet, "movie")
router.register("movie-des", views.MovieDescriptionViewSet, "movie-des")


urlpatterns = [
    path('', include(router.urls)),
]
