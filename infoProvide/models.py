from django.db import models

# Create your models here.
class Provider(models.Model):
    text_name = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
   # total_query = models.IntegerField()
    #pub_date = models.DateTimeField('date published')

    
