
from Auth.serializer import UserSerializer
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers 
from api.models import Contact, Opportunities, Produit, Prospect 

class ProduitSerializer(serializers.ModelSerializer):

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
        
class RetriveContactSerializer(serializers.ModelSerializer):
    prospect = Prospecterializer(read_only=True)
    user =  UserSerializer(read_only=True)

    class Meta:
        model   = Contact
        fields = ('id',   'name' ,'phone' ,'email', 'prospect' , 'user')


class OpportunitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunities
        fields = "__all__"

class RetriveOpportunitiesSerializer(serializers.ModelSerializer):
    prospect = Prospecterializer(read_only=True)
    user =  UserSerializer(read_only=True)
    produit = ProduitSerializer(read_only=True)

    class Meta:
        model   = Opportunities
        fields = ('id', 'name'  ,'phase' ,'description' ,'signatureDate', 'estimatePrice','prospect' , 'user' , 'produit')


