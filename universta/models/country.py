from django.db import models
class Country(models.Model):
    country_name = models.CharField(max_length=50)
    active_status = models.BooleanField(max_length=10, default=1)