from django.db import models

class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.brand} {self.model}'
