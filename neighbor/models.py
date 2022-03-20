from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.
class Neighbor(models.Model) :
  n_name = models.CharField(max_length=35)
  n_location = models.CharField(max_length=35)
  n_image = models.ImageField(upload_to='n_posts/')
  n_title = models.CharField(max_length=100)
  n_post = models.TextField()
  n_author = models.ForeignKey(User, on_delete=models.CASCADE)
  n_date_posted = models.DateTimeField(default=timezone.now)