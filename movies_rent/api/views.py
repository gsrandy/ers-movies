from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins
from movies_rent.models import MovieRent
from .serializers import MovieRentCreateSerializer

class MovieRentCreateApiView(mixins.ListModelMixin,generics.CreateAPIView):
    pass
    permission_classes = (IsAuthenticated,)
    queryset = MovieRent.objects.all()
    serializer_class = MovieRentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(rent_by=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)        

class MovieRentUpdateApiView(generics.UpdateAPIView):
    pass
    permission_classes = (IsAuthenticated,)
    lookup_field       = 'id'
    queryset           = MovieRent.objects.all()