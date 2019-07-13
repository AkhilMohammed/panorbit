from django.db import models

# Create your models here.

class signup(models.Model):

    email = models.EmailField(max_length=30,primary_key=True)
    firstname = models.CharField(max_length=20,default='')
    lastname = models.CharField(max_length=20,default='')
    gender = models.CharField(max_length=10, default='')
    mobile = models.CharField(max_length=30,default='')


class city(models.Model):
    id=models.IntegerField(primary_key=True)
    city=models.CharField(max_length=35,)
    countrycode=models.CharField(max_length=3)
    district=models.CharField(max_length=20)
    population=models.IntegerField(default='0')



    def __str__(self):
        return self.city

class country(models.Model):
    code=models.CharField(max_length=3,primary_key=True)
    name=models.CharField(max_length=53)
    continent=models.CharField(max_length=30)
    region=models.CharField(max_length=50)
    surfaceare=models.DecimalField(max_digits=10,decimal_places=4)
    independentyear=models.IntegerField()
    population=models.IntegerField()
    lifeexpectancy=models.DecimalField(max_digits=80,decimal_places=3)
    gnp=models.DecimalField(max_digits=50,decimal_places=2)
    gnpld=models.DecimalField(max_digits=10,decimal_places=3)
    localname=models.CharField(max_length=50)
    govname=models.CharField(max_length=45)
    headofstat=models.CharField(max_length=60)
    capital=models.IntegerField()
    code2=models.CharField(max_length=3)






