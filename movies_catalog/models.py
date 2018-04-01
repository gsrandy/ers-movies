from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MovieCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    category = models.ForeignKey(MovieCategory, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    image_url = models.CharField(max_length=200)
    rating = models.CharField(max_length=20)
    duration = models.IntegerField()
    director = models.CharField(max_length=50)
    stars = models.CharField(max_length=200)
    release_date = models.DateField()
    trailer_url = models.CharField(max_length=1000)
    rent_amt = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='updated_by')
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.title)

    @property
    def category_name(self):
        return self.category.name

    @property
    def created_by_usr(self):
        return self.created_by.username

    @property
    def updated_by_usr(self):
        return self.updated_by.username     


class RentPackage(models.Model):
    name = models.CharField(max_length=50)
    qty_in_days = models.IntegerField()
    rent_amt = models.DecimalField(max_digits=19, decimal_places=2)