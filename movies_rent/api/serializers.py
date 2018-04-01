from rest_framework import serializers
from movies_rent.models import MovieRent
import datetime

class MovieRentCreateSerializer(serializers.ModelSerializer):
    status_desc = serializers.SerializerMethodField()
    class Meta:
        model = MovieRent
        fields=[
            'id',
            'movie',
            'movie_title',
            'customer_name',
            'rent_total_days',         
            'rent_start_date',
            'rent_end_date',
            'rent_by',
            'rent_at',
            'rent_start_date',
            'rent_end_date',
            'rent_amt',
            'penalty_amt',
            'total_amt',
            'status',
            'returned_at',
            'returned_by',
            'status_desc'
        ]
        read_only_fields=[
            'id',         
            'rent_start_date',
            'rent_end_date',
            'rent_by',
            'rent_at',
            'rent_start_date',
            'rent_end_date',
            'rent_amt',
            'penalty_amt',
            'total_amt',
            'status',
            'returned_at',
            'returned_by',
            'status_desc'
        ]

    def get_status_field(self,obj):
        current_date = datetime.datetime.now().date()
        if obj.status == 'A' and current_date > obj.rent_end_date:
            return 'D'
        else:
            return obj.status

    def get_status_desc(self , obj):
        current_date = datetime.datetime.now().date()
        if obj.status == 'A' and current_date > obj.rent_end_date:
            return 'Delayed'
        elif obj.status == 'A':
            return 'Active'
        elif obj.status == 'R':
            return 'Returned'    

class MovieRentUpdateSerializer(serializers.ModelSerializer):
    status_desc = serializers.SerializerMethodField()
    class Meta:
        model = MovieRent
        fields=[
           'id',
            'movie',
            'movie_title',
            'customer_name',
            'rent_total_days',         
            'rent_start_date',
            'rent_end_date',
            'rent_by',
            'rent_at',
            'rent_start_date',
            'rent_end_date',
            'rent_amt',
            'penalty_amt',
            'total_amt',
            'status',
            'returned_at',
            'returned_by',
            'status_desc' 
        ]
        read_only_fields=[
            'id',
            'movie',
            'movie_title',
            'customer_name',
            'rent_total_days',         
            'rent_start_date',
            'rent_end_date',
            'rent_by',
            'rent_at',
            'rent_start_date',
            'rent_end_date',
            'rent_amt',
            'penalty_amt',
            'total_amt',
            'status',
            'returned_at',
            'returned_by',
            'status_desc' 
        ]

    def get_status_field(self,obj):
        current_date = datetime.datetime.now().date()
        if obj.status == 'A' and current_date > obj.rent_end_date:
            return 'D'
        else:
            return obj.status

    def get_status_desc(self , obj):
        current_date = datetime.datetime.now().date()
        if obj.status == 'A' and current_date > obj.rent_end_date:
            return 'Delayed'
        elif obj.status == 'A':
            return 'Active'
        elif obj.status == 'R':
            return 'Returned'
   