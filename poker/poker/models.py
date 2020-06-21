from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Table Model
class Tables(models.Model):
    code = models.IntegerField() #Room Code can be maximum 16 characters long
    players = models.ManyToManyField(User) #The players for each table, many to many field allows multiple users to be on one table

    def __str__(self):
        return "Table Code: {0}, Players: {1}".format(self.code,self.players.all()) #toStr method
