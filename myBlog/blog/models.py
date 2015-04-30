from django.db import models

# Create your models here.
class blogposts(models.Model):
    # Title of the post
    Title = models.CharField(max_length=200)
    # The time when it was published
    Pub_date = models.DateTimeField('date published')
    # A short description of the post
    Description = models.CharField(max_length=200)
    # Link to the text file of the post (stored in static directory)
    Text_link = models.CharField(max_length=200)
