from django.db import models

# Create your models here.
class Review(models.Model):
    score = models.IntegerField(max_length= 1, blank=False, null=False)
    comment = models.CharField(max_length= 280, blank=False, null=False)