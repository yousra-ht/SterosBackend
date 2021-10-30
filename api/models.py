from Auth.models import *
from django.db import models

from Auth.models import NewUser

class TypeProduit(models.Model):
    name = models.CharField(max_length=150)
    delete = models.BooleanField(null=True)
    description = models.TextField(null=True , blank=True)

class Produit(models.Model) :
    
    designation = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    pointFaible = models.TextField()
    pointFort=models.TextField()
    image = models.ImageField(upload_to='images' , null=True)
    delete = models.BooleanField(null=True)
    code = models.CharField(max_length=100, unique=True )
    type = models.ForeignKey(TypeProduit , on_delete=models.SET_NULL , null=True) 
  




    def __str__(self):
        # This method defines what the string representation an instance.
        return f'{self.name}: ${self.phone}'
 




class Pays (models.Model)  :
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True )
    delete = models.BooleanField(null=True)
    # Ville  = models.ManyToManyField(Ville ,  blank=True  )
    
class Ville (models.Model)  :
    ville = models.CharField(max_length=100)
    adresse = models.CharField(max_length=150)
    Pays = models.ForeignKey(Pays , on_delete=models.CASCADE  ) 
    description = models.TextField(null=True, blank=True )
    delete = models.BooleanField(null=True)



class competition(models.Model) :
    
    entreprise = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    pointFaible = models.TextField()
    pointFort=models.TextField()
    image = models.ImageField(upload_to='images' , null=True)
    delete = models.BooleanField(null=True)
    # code = models.CharField(max_length=100, unique=True , null=True , blank=True)
    type = models.CharField(max_length=100 , null=True , blank=True)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL , null=True) 
  
class Prospect(models.Model) :
    
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    fax= models.CharField(max_length=150 , null=True) 
    size= models.PositiveIntegerField(null=True)
    delete = models.BooleanField(null=True)
    pays = models.ForeignKey(Pays, on_delete=models.SET_NULL , null=True)
    Ville = models.ForeignKey(Ville, on_delete=models.SET_NULL , null=True)
    type = models.CharField(max_length=150 , null=True) 
    codePostal = models.CharField(max_length=100 , null=True)
    banque = models.CharField(max_length=200  , null=True)
    Rib = models.CharField(max_length=200  , null=True)
    activity  = models.CharField(max_length=200  , null=True)
    langue =   models.CharField(max_length=200  , null=True)
    description = models.TextField(null=True)





class Contact(models.Model) :
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    function = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=150)
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL , null=True) 
    prospect = models.ForeignKey(Prospect, on_delete=models.SET_NULL , null=True) 
    delete = models.BooleanField(null=True)
    principale  = models.BooleanField(null=True)
    birthday = models.CharField(max_length=150, null=True)
    lastname = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    adresse = models.CharField(max_length=150 ,null=True )
    pays = models.ForeignKey(Pays, on_delete=models.SET_NULL , null=True)
    Ville = models.ForeignKey(Ville, on_delete=models.SET_NULL , null=True)

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
    Contact = models.ManyToManyField(Contact ,  blank=True )

class Action(models.Model) :
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=150 , blank=True)
    startDate = models.CharField(max_length=150)
    endDate = models.CharField(max_length=150 , blank=True )
    description = models.TextField(null=True , blank=True )
    Contact = models.ManyToManyField(Contact ,  blank=True )
    contents = models.TextField(blank=True , null=True)
    type = models.CharField(max_length=150)
    place = models.CharField(max_length=150 , blank=True , null=True)
    Opportunity = models.ForeignKey(Opportunities, on_delete=models.CASCADE , null=True , default='')
    user= models.ForeignKey(NewUser, on_delete=models.CASCADE , null=True , default='')
   

class Goals(models.Model) :
    chiffre = models.CharField(max_length=150)
    recouvrement = models.CharField(max_length=150 , blank=True)
    startDate = models.CharField(max_length=150)
    endDate = models.CharField(max_length=150 , blank=True )
    objectif = models.TextField(null=True , blank=True )
    user= models.ForeignKey(NewUser, on_delete=models.CASCADE , null=True , default='')


