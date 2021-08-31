from Auth.models import NewUser
from django.db import models

class Produit(models.Model) :
    
    designation = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    pointFaible = models.TextField()
    pointFort=models.TextField()
    image = models.ImageField(upload_to='images')

class Prospect(models.Model) :
    
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    fax= models.CharField(max_length=150)
    size= models.PositiveIntegerField()

class Contact(models.Model) :
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL , null=True) 
    prospect = models.ForeignKey(Prospect, on_delete=models.SET_NULL , null=True) 


    
class Opportunities(models.Model) :
    name = models.CharField(max_length=100)
    estimatePrice = models.PositiveIntegerField()
    signatureDate = models.CharField(max_length=150)
    description = models.TextField()
    phase = models.CharField(max_length=150)
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL , null=True) 
    prospect = models.ForeignKey(Prospect, on_delete=models.SET_NULL , null=True) 
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL , null=True) 
   
class Action(models.Model) :
    title = models.CharField(max_length=150)
    startDate = models.CharField(max_length=150)
    starttime = models.CharField(max_length=150)
    endtime = models.CharField(max_length=150 ,  null=True )
    duration = models.CharField(max_length=150 , null=True)
    description = models.TextField(null=True)
    contents = models.TextField(null=True)
    type = models.CharField(max_length=150)
    place = models.CharField(max_length=150 , null=True)
    Opportunity = models.ForeignKey(Opportunities, on_delete=models.CASCADE , null=True , default='')


  
