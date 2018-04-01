

from django.conf.urls import url
from django.contrib import admin
from .views import MovieCategoryListApiView, MovieListApiView, RentPackageListApiView

urlpatterns = [
    url(r'^movies/', MovieListApiView.as_view(), name="movies-list"),
    url(r'^movies_categories/', MovieCategoryListApiView.as_view(), name="movies-categories-list"),
    url(r'^rent_packages/', RentPackageListApiView.as_view(), name="rent-packages-list"),
]