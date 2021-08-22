
from rest_framework import authentication
from rest_framework.serializers import ModelSerializer
from api.models import Contact, Opportunities, Produit, Prospect
from  rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializer


    
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