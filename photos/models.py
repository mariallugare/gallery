from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name

class Photo(models.Model):
   
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = CloudinaryField('image')
    description = models.TextField()
    location = models.TextField( null=True,blank=True)
    def __str__(self):
        return self.description
   
