from django.db import models
from Admin.models import tbl_movie
# Create your models here.

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    movie=models.ForeignKey(tbl_movie,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)