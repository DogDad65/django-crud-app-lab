from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="bikes", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
