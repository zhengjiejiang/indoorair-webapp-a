
from django.db import models
from django.contrib.auth.models import User
class Tag(models.Model):
   name = models.CharField(max_length=255)
   def __str__(self):
       return self.name



class Instrument(models.Model):
   user = models.ForeignKey(
       User,
       on_delete=models.CASCADE
   )
   name = models.CharField(max_length=255)
   tags = models.ManyToManyField(to="Tag")
   def __str__(self):
       return self.name + " " + str(self.user)



class TimeSeriesDatum(models.Model):
   instrument = models.ForeignKey( # one-to-many
       to='Instrument',
       on_delete=models.CASCADE
   )
   value = models.FloatField()
   time = models.DateTimeField()
   def __str__(self):
       return str(self.instrument) + " is " + str(self.value) + " at " + str(self.time)






class Manufacturer(models.Model):
    part = models.ManyToManyField(to="Part")
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length = 222)
    manufacturer= models.ForeignKey(
    to='Manufacturer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Part(models.Model):
    name = models.CharField(max_length = 222)
    carmodel= models.ForeignKey(
        to='CarModel',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
