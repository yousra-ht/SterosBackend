

from rest_framework import authentication
from rest_framework.serializers import ModelSerializer
from api.models import Action, Contact, Opportunities, Produit, Prospect
from  rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializer
from django.db.models import Sum


    
class ProduitListe(ListCreateAPIView):
        queryset = Produit.objects.all()
        serializer_class =serializer.ProduitSerializer
        pagination_class = None
        Produit.objects
     

class ProduitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =serializer.ProduitSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Produit.objects.filter(id=self.kwargs.get('pk' , None)) 
 
class ProspectListe(ListCreateAPIView):
        queryset = Prospect.objects.all()
        serializer_class =serializer.Prospecterializer
        pagination_class = None
        Prospect.objects


class ContactListe(ListCreateAPIView):
        queryset = Contact.objects.all()
        permission_classes = [IsAuthenticated]
        pagination_class = None
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.ContactSerializer
                return serializer.RetriveContactSerializer 


class OpportunitiesListe(ListCreateAPIView):
        queryset = Opportunities.objects.all()
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeWinning(ListCreateAPIView):
        queryset = Opportunities.objects.all().filter(phase='Gagnée')
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeNopa(ListCreateAPIView):
        queryset = Opportunities.objects.all()
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeQualification(ListCreateAPIView):
        queryset = Opportunities.objects.all().filter(phase='Qualification')
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer


class OpportunitiesListeEtude(ListCreateAPIView):
        queryset = Opportunities.objects.all().filter(phase='Etude de besoins')
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeProposition(ListCreateAPIView):
        queryset = Opportunities.objects.all().filter(phase='Proposition commerciale')
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer


class OpportunitiesListeNegociation(ListCreateAPIView):
        queryset = Opportunities.objects.all().filter(phase='Négociation')
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeGagnee(ListCreateAPIView):
        queryset = Opportunities.objects.all().filter(phase='Gagnée')
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListePerdue(ListCreateAPIView):
        queryset = Opportunities.objects.all().filter(phase='Perdue')
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer


class OpportunitiesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =serializer.OpportunitiesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Opportunities.objects.filter(id=self.kwargs.get('pk' , None)) 

class SumQualification():
        permission_classes = [IsAuthenticated]
        sum = Opportunities.objects.all().filter(phase='Qualification').aggregate(Sum('estimatePrice'))


class SumQualification(serializer.OpportunitiesSerializer):
    total_pieces = serializer.OpportunitiesSerializer
  
    class Meta:
        model = Opportunities
        fields = '__all__'

    def get_total_pieces(self, obj):
        totalpieces = Opportunities.objects.all().filter(phase='Qualification').aggregate(Sum('estimatePrice'))
        return totalpieces["total_pieces"]
#     def get_total_price(self, obj):
#         totalprice = Catalog.objects.all().aggregate(total_price=Sum('per_piece_price'))
#         return totalprice["total_price"]



class OpportunityDetaills(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
       
        return serializer.RetriveOpportunitiesSerializer
    def get_queryset(self): 
        return Opportunities.objects.filter(id=self.kwargs.get('pk' , None))  

class emailListe(ListCreateAPIView):
        serializer_class =serializer.ActionSerializer
        pagination_class = None
        def get_queryset(self): 
       
                return Action.objects.all().filter(type='email' , Opportunity_id= self.kwargs.get('pk' , None)  )
       
class callListe(ListCreateAPIView):
        serializer_class =serializer.ActionSerializer
        pagination_class = None
        def get_queryset(self): 
       
                return Action.objects.all().filter(type='phone call' , Opportunity_id= self.kwargs.get('pk' , None)  )
       
class meetingListe(ListCreateAPIView):
        serializer_class =serializer.ActionSerializer
        pagination_class = None
        def get_queryset(self): 
       
                return Action.objects.all().filter(type='meeting' , Opportunity_id= self.kwargs.get('pk' , None)  )
       
                       
class ActionListe(ListCreateAPIView):
        queryset = Action.objects.all()
        serializer_class =serializer.ActionSerializer
        pagination_class = None
        Action.objects      