from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('CONVERTIBLE', 'Convertible'),
    ]
    type = models.CharField(max_length=15, 
                choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2024,
        validators=[
            MaxValueValidator(2025),
            MinValueValidator(2015)
        ])
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation
