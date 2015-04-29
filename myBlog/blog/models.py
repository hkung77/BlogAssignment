from django.db import models

# Create your models here.
class blogposts(models.Model):
    Title = models.CharField(max_length=200)
    Pub_date = models.DateTimeField('date published')
    Description = models.CharField(max_length=200)
    Text_link = models.CharField(max_length=200)
    Image_link = models.CharField(max_length=200)
