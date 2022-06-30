from django.db import models

# Create your models here.

class BmiMeasurement(models.Model):
    height_in_meters = models.FloatField()
    weight_in_kg = models.FloatField()
    measured_at = models.DateField()

    def bmi(self):
        return self.weight_in_kg / self.height_in_meters ** 2
