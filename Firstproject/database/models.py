from django.db import models

# Create your models here.
class userdata (models.Model):
    username = models.CharField(max_length=50 , null=True)
    email = models.EmailField(max_length=254 , null=True)