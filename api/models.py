from Auth.models import NewUser
from django.db import models


class Produit(models.Model) :
    
    designation = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    pointFaible = models.TextField()
    pointFort=models.TextField()
    image = models.ImageField(upload_to='images' , null=True)
    delete = models.BooleanField(null=True)

class Prospect(models.Model) :
    
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    fax= models.CharField(max_length=150 , null=True) 
    size= models.PositiveIntegerField()
    delete = models.BooleanField(null=True)

class Contact(models.Model) :
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    function = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=150)
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL , null=True) 
    prospect = models.ForeignKey(Prospect, on_delete=models.SET_NULL , null=True) 
    delete = models.BooleanField(null=True)

    def __str__(self):
        # This method defines what the string representation an instance.
        return f'{self.name}: ${self.phone}'
 
class Opportunities(models.Model) :
    name = models.CharField(max_length=100)
    estimatePrice = models.FloatField()
    signatureDate = models.CharField(max_length=150)
    creationDate = models.CharField(max_length=150 , null=True)
    description = models.TextField()
    phase = models.CharField(max_length=150)
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL , null=True) 
    prospect = models.ForeignKey(Prospect, on_delete=models.SET_NULL , null=True) 
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL , null=True) 
    delete = models.BooleanField(null=True)
   
class Action(models.Model) :
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=150 , blank=True)
    startDate = models.CharField(max_length=150)
    endDate = models.CharField(max_length=150 , blank=True )
    description = models.TextField(null=True)
    Contact = models.ManyToManyField(Contact ,  blank=True )
    contents = models.TextField(blank=True , null=True)
    type = models.CharField(max_length=150)
    place = models.CharField(max_length=150 , blank=True , null=True)
    Opportunity = models.ForeignKey(Opportunities, on_delete=models.CASCADE , null=True , default='')
    user= models.ForeignKey(NewUser, on_delete=models.CASCADE , null=True , default='')

   
  
