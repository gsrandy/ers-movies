from django.contrib import admin
from .models import MovieCategory, Movie, RentPackage

# Register your models here.

admin.site.register(MovieCategory)
admin.site.register(Movie)
admin.site.register(RentPackage)

