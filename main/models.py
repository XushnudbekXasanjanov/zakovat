from django.db import models


class RegistrationTeam(models.Model):
    fullname = models.CharField(max_length=255)
    team_name = models.CharField(max_length=50,unique=True)
    username = models.CharField(max_length=255)
    count = models.IntegerField()
    STATUS = (
        (1,"Ro'yhatdan o'tgan"),
        (2,"Ro'yhatdan o'tmagan")
    )
    choice = models.IntegerField(choices=STATUS,default=1)
