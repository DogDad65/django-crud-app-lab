from django.db import models
from django.urls import reverse

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
    ('W', 'Wax Chain'),
    ('B', 'Brake Check')
)

UPGRADE_TYPES = [
    ('PM', 'Power Meter'),
    ('CS', 'Cassette'),
    ('SH', 'Shifters'),
    ('HB', 'Handlebars'),
    ('CR', 'Carbon Rims'),
]

class Maintenance(models.Model):
    date = models.DateField('Maintenance Date')
    maintenance_type = models.CharField(
        max_length=1,
        choices=MAINTENANCE_TYPES,
        default=MAINTENANCE_TYPES[0][0]
    )
    notes = models.TextField(blank=True, null=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_maintenance_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']  # Newest maintenance first

class Upgrade(models.Model):
    type = models.CharField(
        max_length=2,
        choices=UPGRADE_TYPES,
        default='PM'  # Default set to 'PM' if needed, or remove if no default is desired
    )
    description = models.TextField(blank=True)
    date_installed = models.DateField()
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} installed on {self.date_installed}"

    def get_absolute_url(self):
        return reverse('upgrade_detail', kwargs={'pk': self.pk})
