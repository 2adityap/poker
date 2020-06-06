from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tables(models.Model):
    code = models.CharField(max_length=16)
    players = models.ManyToManyField(User)

    def __str__(self):
        return "Table Code: {0}, Players: {1}".format(self.code,self.players.all())
    
