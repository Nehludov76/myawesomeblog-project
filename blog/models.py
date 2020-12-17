from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog_images/')