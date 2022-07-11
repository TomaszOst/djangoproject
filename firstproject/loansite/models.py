from email.headerregistry import Address
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age= models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(80)])
 
class ClientInfo(models.Model):
    #customer= models.ForeignKey(Client)
    zip_code= models.CharField(max_length=5, default="43701")
    address= models.CharField(max_length=200)
    marital_status= models.BooleanField()
    #forma zatrudnienia
    amount_of_income= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100000)])
    date_of_commencement_of_work= models.DateField()
    number_of_dependent_children=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(15)])

#class Scoring(models.Model):



    

