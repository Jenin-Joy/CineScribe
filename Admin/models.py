from django.db import models

# Create your models here.

class tbl_genre(models.Model):
    genre_name = models.CharField(max_length=30)

class tbl_cruetype(models.Model):
    cruetype_name = models.CharField(max_length=30)

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_contact = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=20)

class tbl_movie(models.Model):
    movie_title = models.CharField(max_length=50)
    movie_release_date = models.DateField()
    movie_description = models.CharField(max_length=100)
    movie_poster = models.FileField(upload_to="Assets/Movie/")
    movie_link = models.CharField(max_length=500)
    genre = models.ForeignKey(tbl_genre, on_delete=models.CASCADE)

class tbl_crue(models.Model):
    crue_name = models.CharField(max_length=30)
    crue_photo = models.FileField(upload_to="Assets/Crue/")
    cruetype = models.ForeignKey(tbl_cruetype, on_delete=models.CASCADE)
    movie = models.ForeignKey(tbl_movie, on_delete=models.CASCADE)