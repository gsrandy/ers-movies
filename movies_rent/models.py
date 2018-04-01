from django.db import models
from movies_catalog.models import Movie
from django.contrib.auth.models import User
import datetime

# Create your models here.

class MovieRent(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50) 
    rent_by = models.CharField(max_length=50)
    rent_at = models.DateTimeField(auto_now_add=True)
    rent_start_date = models.DateField()
    rent_end_date = models.DateField()
    rent_total_days = models.IntegerField()
    rent_amt = models.DecimalField(max_digits=19, decimal_places=2)
    penalty_amt = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    total_amt = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    status = models.CharField(max_length=2)
    returned_at = models.DateTimeField(null=True)
    returned_by = models.CharField(max_length=50,default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
           self.set_rent_data()
        elif self.status != 'R':
            self.status = 'R'
            self.calc_penalty_amt()   
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def set_rent_data(self):
        self.status = 'A'
        self.rent_at = datetime.date
        self.rent_start_date = datetime.datetime.now().date()
        self.rent_end_date = self.rent_start_date + datetime.timedelta(days=self.rent_total_days)
        self.rent_amt = self.movie.rent_amt
        self.total_amt = self.rent_amt

    def calc_penalty_amt(self):
        current_date = datetime.datetime.now().date()
        if current_date > self.rent_end_date:
            self.penalty_amt = self.rent_amt * 0.05
            self.total_amt = self.rent_amt + self.penalty_amt    


    @property
    def movie_title(self):
        return self.movie.title    
    
    def __str__(self):
        return "Id: {}, customer: {}".format(str(self.id) , str(self.customer_name))
