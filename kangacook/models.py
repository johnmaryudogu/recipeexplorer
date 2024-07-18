from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField() 
    image_url = models.URLField()

    def __str__(self):
        return self.name
