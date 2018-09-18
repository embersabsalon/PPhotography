from django.db import models

# Create your models here.
class Photo(models.Model):
    photoid = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100) 
    likes = models.DecimalField(max_digits = 9, decimal_places=0, default=0)
    photographer = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, default="A sample image.")
    img_url = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.name
    
class Photographer(models.Model):
    photographerid = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    emailaddress = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, default="Hi!")
    img_url = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.name