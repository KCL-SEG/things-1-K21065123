from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30,
    unique= True,
    blank= False)
    
    description = models.CharField(max_length=120, blank= True)
    quantity= models.IntegerField(blank=False,
                                  validators=[MinValueValidator(limit_value=0),
                                      MaxValueValidator(limit_value=100)]) 


