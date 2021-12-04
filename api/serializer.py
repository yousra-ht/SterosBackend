
from rest_framework.fields import DecimalField
from rest_framework.validators import UniqueValidator
from Auth.serializer import UserSerializer
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers 
from api.models import *


class LangueSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Langues
        fields = "__all__" 


class ProduitSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[ UniqueValidator( queryset= Produit.objects.all(),lookup='iexact')])
    class Meta:
        model = Produit
        fields = "__all__"



class Prospecterializer(serializers.ModelSerializer):

    class Meta:
        model = Prospect 
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"
        



class OpportunitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunities
        fields = "__all__"

class RetriveOpportunitiesSerializer(serializers.ModelSerializer):
    prospect = Prospecterializer(read_only=True)
    user =  UserSerializer(read_only=True)
    produit = ProduitSerializer(read_only=True)
    Contact = ContactSerializer(read_only=True ,many=True)

    class Meta:
        model   = Opportunities
        ordering = ('creationDate',)
        fields = ('id', 'name'  ,'phase' ,'description' ,'signatureDate','creationDate', 'estimatePrice','prospect' , 'user' , 'produit' , 'delete' , 'Contact')


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Action
        fields = "__all__"


class RetriveActionbbbbSerializer(serializers.ModelSerializer):
    Contact = ContactSerializer(read_only=True,many=True)
    user =  UserSerializer(read_only=True)
    Opportunity =RetriveOpportunitiesSerializer(read_only=True)


    class Meta:
        model   = Action
        fields = ('id', 'title'  ,'startDate' ,'endDate' ,'status','description', 'contents','type' , 'place' , 'Opportunity','Contact', 'user' )

class PaysSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Pays
        fields = "__all__"

class VilleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ville
        fields = "__all__"

class RetriveProspecterializer(serializers.ModelSerializer):
    pays = PaysSerializer(read_only=True)
    Ville = VilleSerializer(read_only =True)
    langue = LangueSerializer(read_only =True)
    class Meta:
        model = Prospect 
        fields = ('id',   'name' ,'adress' ,'phone', 'email','fax' , 'size', 'delete' ,'Ville',  'pays', 'type' ,'codePostal' , 'banque', 'Rib' , 'activity', 'langue', 'description' , 'Tel' ) 


class RetriveVilleSerializer(serializers.ModelSerializer):
    Pays = PaysSerializer(read_only=True)
    class Meta:
        model =  Ville
        fields =('id','Pays' , 'ville' ,'delete'  ,'adresse' ,'description')

class competitionSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(validators=[ UniqueValidator( queryset= Produit.objects.all(),lookup='iexact')])
    class Meta:
        model = competition
        fields = "__all__"
        
class RetrivecompetitionSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(validators=[ UniqueValidator( queryset= Produit.objects.all(),lookup='iexact')])
    produit = ProduitSerializer(read_only=True)
    class Meta:
        model = competition
        fields =('id','entreprise' , 'designation' ,'delete'  ,'description' ,'prix','pointFaible' , 'pointFort' ,'image'  ,'type', 'produit')


class TypeProduitSerializer(serializers.ModelSerializer):
     class Meta:
        model = TypeProduit
        fields = "__all__"


class RetriveProduitSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[ UniqueValidator( queryset= Produit.objects.all(),lookup='iexact')])
    type =TypeProduitSerializer(read_only=True)
    class Meta:
        model = Produit
        fields =('id' , 'designation' ,'delete'  ,'description' ,'prix','pointFaible' , 'pointFort' ,'image'  ,'type' , 'code')

class RetriveContactSerializer(serializers.ModelSerializer):
    prospect = Prospecterializer(read_only=True)
    user =  UserSerializer(read_only=True)
    pays = PaysSerializer(read_only=True)
    Ville = VilleSerializer(read_only =True)

    class Meta:
        model   = Contact
        fields = ('id',   'name' ,'phone' ,'email', 'function','prospect' , 'user' , 'birthday' ,'lastname' ,'description' , 'adresse' ,'pays','Ville' , 'Tel' )

class GoalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goals
        fields = "__all__"


