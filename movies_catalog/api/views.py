from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from movies_catalog.models import MovieCategory, Movie, RentPackage
from .serializers import MoviesSerializer, MovieCategorySerializer, RentPackageSerializer

class MovieCategoryListApiView(generics.ListAPIView):
    pass
    permission_classes = (IsAuthenticated,)
    lookup_field        = 'id'
    queryset            = MovieCategory.objects.all()
    serializer_class    = MovieCategorySerializer

class MovieListApiView(generics.ListAPIView):
    pass
    permission_classes = (IsAuthenticated,)
    lookup_field        = 'id'
    queryset            = Movie.objects.all()
    serializer_class    = MoviesSerializer


class RentPackageListApiView(generics.ListAPIView):
    pass
    permission_classes = (IsAuthenticated,)
    lookup_field        = 'id'
    queryset            = RentPackage.objects.all()
    serializer_class    = RentPackageSerializer
