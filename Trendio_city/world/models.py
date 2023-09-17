from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(unique=True, max_length=30)
    # a country can hold several languages, but to avoid creating another model im only adding one 
    language = models.CharField(max_length=20) 

    
    def total_population(self):
        # Calculate and return the total population of the country
        return sum(city.population for city in self.cities.all())
    
    
    def __str__(self) -> str:
        return self.country_name
    
    
    
class City(models.Model):
    city_name = models.CharField(unique=True, max_length=30)
    country_fk = models.ForeignKey(Country, related_name="cities", on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.city_name
    
    