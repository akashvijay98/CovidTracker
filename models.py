from django.db import models

# Create your models here.
class covid_data(models.Model):
    
    date = models.CharField(max_length=100,default="00/00")
    time = models.CharField(max_length=100,default="00:00")
    state = models.CharField(max_length=100,default="karnatak")
    ci = models.CharField(max_length=100,default= '-')#confirmed Indian
    cf = models.CharField(max_length=100,default='-')#cinfirmed Foreigner
    cured = models.IntegerField(blank=True)
    deaths = models.IntegerField(blank=True)
    confirmed = models.IntegerField(blank=True)



    



def __str__(self):
    return self.sno + ' ' + self.state