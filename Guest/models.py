from django.db import models

# Create your models here.

class tbl_user(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)
    user_status = models.IntegerField(default=0)