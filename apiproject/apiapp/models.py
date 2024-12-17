from django.db import models

# Create your models here.

class Book(models.Model):
    
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_data=models.DateField()

    def __str__(self):
        return self.title