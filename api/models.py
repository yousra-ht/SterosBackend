from Auth.models import *
from django.db import models

from Auth.models import NewUser

class TypeProduit(models.Model):
    name = models.CharField(max_length=150 , unique=True )
    delete = models.BooleanField()
    description = models.TextField(null=True , blank=True)

class Produit(models.Model) :
    
    designation = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(decimal_places=3, max_digits=12)
    pointFaible = models.TextField()
    pointFort=models.TextField()
    image = models.ImageField(upload_to='images' , null=True)
    delete = models.BooleanField()
    code = models.CharField(max_length=100, unique=True )
    type = models.ForeignKey(TypeProduit ,  on_delete=models.CASCADE )
    user = models.ForeignKey(NewUser,  null=True ,on_delete= models.SET_NULL ) 
  




    def __str__(self):
        # This method defines what the string representation an instance.
        return f'{self.name}: ${self.phone}'
 




class Pays (models.Model)  :
    name = models.CharField(max_length=100 , unique=True )
    description = models.TextField(null=True, blank=True )
    delete = models.BooleanField()
    # Ville  = models.ManyToManyField(Ville ,  blank=True  )

class Langues (models.Model)  :
    langue = models.CharField(max_length=100 , unique=True)
    description = models.TextField(null=True, blank=True )
    delete = models.BooleanField()
    # Ville  = models.ManyToManyField(Ville ,  blank=True  )



class Ville (models.Model)  :
    ville = models.CharField(max_length=100 ,   unique=True)
    Pays = models.ForeignKey(Pays , on_delete=models.CASCADE  ) 
    description = models.TextField(null=True, blank=True )
    delete = models.BooleanField()

class Adresses (models.Model)  :
    adresse = models.CharField(max_length=100 ,   unique=True)
    ville = models.ForeignKey( Ville , on_delete=models.CASCADE  ) 
    description = models.TextField(null=True, blank=True )
    delete = models.BooleanField()    

class competition(models.Model) :
    
    entreprise = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    pointFaible = models.TextField()
    pointFort=models.TextField()
    image = models.ImageField(upload_to='images' , null=True)
    delete = models.BooleanField()
    # code = models.CharField(max_length=100, unique=True , null=True , blank=True)
    type = models.CharField(max_length=100 , null=True , blank=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE ,) 
  
class Prospect(models.Model) :
    
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    Tel= models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=150)
    fax= models.CharField(max_length=150 , null=True , blank=True) 
    size= models.PositiveIntegerField()
    delete = models.BooleanField()
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE )
    Ville = models.ForeignKey(Ville, on_delete=models.CASCADE ,  )
    type = models.CharField(max_length=150 ,  null=True) 
    codePostal = models.CharField(max_length=100 , null=True)
    banque = models.CharField(max_length=200  , null=True)
    Rib = models.CharField(max_length=200  , null=True)
    activity  = models.CharField(max_length=200 )
    langue =  models.ForeignKey(Langues, on_delete=models.CASCADE )
    description = models.TextField(null=True)





class Contact(models.Model) :
    name = models.CharField(max_length=100 )
    phone = models.CharField(max_length=100 ) 
    Tel= models.CharField(max_length=150, blank=True)
    function = models.CharField(max_length=200 )
    email = models.CharField(max_length=150 )
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE  ) 
    prospect = models.ForeignKey(Prospect,  on_delete=models.CASCADE ) 
    delete = models.BooleanField(default=False)
    principale  = models.BooleanField(null=True)
    birthday = models.CharField(max_length=150  )
    lastname = models.CharField(max_length=100 )
    description = models.TextField(null=True)
    adresse = models.CharField(max_length=150  )
    pays = models.ForeignKey(Pays,  on_delete=models.CASCADE  )
    Ville = models.ForeignKey(Ville,  on_delete=models.CASCADE  )

class Opportunities(models.Model) :
    name = models.CharField(max_length=100)
    estimatePrice =  models.DecimalField(decimal_places=3, max_digits=12)
    signatureDate = models.CharField(max_length=150)
    creationDate = models.CharField(max_length=150 )
    description = models.TextField(null=True , blank=True)
    phase = models.CharField(max_length=150)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE ) 
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE ) 
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE) 
    delete = models.BooleanField()
    Contact = models.ManyToManyField(Contact)

class Action(models.Model) :
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=150 )
    startDate = models.CharField(max_length=150)
    endDate = models.CharField(max_length=150  )
    description = models.TextField(null=True , blank=True )
    Contact = models.ManyToManyField(Contact  )
    contents = models.TextField(blank=True , null=True)
    type = models.CharField(max_length=150)
    place = models.CharField(max_length=150 , blank=True , null=True)
    Opportunity = models.ForeignKey(Opportunities, on_delete=models.CASCADE )
    user= models.ForeignKey(NewUser, on_delete=models.CASCADE )

   

class Goals(models.Model) :
    chiffre = models.CharField(max_length=150)
    recouvrement = models.CharField(max_length=150 , blank=True)
    startDate = models.CharField(max_length=150)
    endDate = models.CharField(max_length=150 , blank=True )
    objectif = models.TextField(null=True , blank=True )
    user= models.ForeignKey(NewUser, on_delete=models.CASCADE , null=True , default='')


