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
    
# Define a tuple of choices for maintenance types
MAINTENANCE_TYPES = (
    ('C', 'Chain Replacement'),
    ('T', 'Tire Replacement'),
    ('O', 'Oil Change'),
    ('B', 'Brake Check')
)

class Maintenance(models.Model):
    date = models.DateField('Maintenance Date')
    maintenance_type = models.CharField(
        max_length=1,
        choices=MAINTENANCE_TYPES,
        default=MAINTENANCE_TYPES[0][0]
    )
    notes = models.TextField(blank=True, null=True)
    # Link each maintenance record to a specific bike
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_maintenance_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']  # Newest maintenance first
