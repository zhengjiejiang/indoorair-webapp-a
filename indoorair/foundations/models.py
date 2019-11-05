from django.db import models
from django.contrib.auth.models import User



class Instrument(models.Model):
    user = models.ForeignKey(# one-to-many
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name + " " + str(self.user)




class Sensor(models.Model):
    instrument = models.ForeignKey( # one-to-many
        to='Instrument',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name +" " + str(self.instrument)




class TimeSeriesDatum(models.Model):
    instrument = models.ForeignKey( # one-to-many
        to='Sensor',
        on_delete=models.CASCADE
    )
    value = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.sensor) + " is " + str(self.value) + " at " + str(self.time)
