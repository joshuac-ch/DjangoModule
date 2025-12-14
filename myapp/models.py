from django.db import models

# Create your models here.
class Task(models.Model):
    nombre=models.CharField(max_length=200)
    descri=models.TextField()
    
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    username=models.CharField(max_length=200)
    profile=models.CharField(max_length=200)

    def __str__(self):
        return self.username