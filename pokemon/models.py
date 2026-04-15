from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    imagen = models.URLField()
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    base_experience = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
