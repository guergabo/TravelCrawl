from django.db import models  # inheriting from the models class to connect to db.
import csv

### Airport Class for the search bar ###
class Airport(models.Model):
    city_name = models.CharField(max_length=250)
    country_name = models.CharField(max_length=250)
    iata_code = models.CharField(max_length=3)

    def __str__(self):
        text = f"{self.city_name}, {self.country_name}, {self.iata_code}"
        return text

