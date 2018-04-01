
from rest_framework import serializers
from movies_catalog.models import Movie, MovieCategory, RentPackage
from movies_rent.models import MovieRent

class MoviesSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = [
            'id',
            'status',
            'category',
            'category_name',
            'title',
            'description',
            'image_url',
            'rating',
            'trailer_url',
            'director',
            'stars',
            'release_date',
            'duration',
            'rent_amt'
        ]

    def get_status(self, obj):
        movie_rents = MovieRent.objects.filter(movie_id=obj.id,status__exact='A')
        print(movie_rents)
        if movie_rents:
            return 'R'
        else:
            return 'A'    


class MovieCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategory
        fields = [
            'id',
            'name',
        ]

class RentPackageSerializer(serializers.ModelSerializer):        
    class Meta:
        model = RentPackage
        fields = [
            'id',
            'name',
            'qty_in_days',
            'rent_amt',
        ]