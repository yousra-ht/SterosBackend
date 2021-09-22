

from django.db.models import aggregates
from django.db.models.aggregates import Avg, Count
from django.db.models.query import InstanceCheckMeta
from django.http import response
from rest_framework import authentication
from rest_framework import generics
from rest_framework.fields import FloatField
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from api.models import Action, Contact, Opportunities, Produit, Prospect
from  rest_framework.generics import (GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializer
from django.db.models import Sum
from CRMBackend.permissions import AuthorAllStaffAllButEditOrReadOnly

    
class ProduitListe(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        queryset = Produit.objects.filter(delete = False)
        serializer_class =serializer.ProduitSerializer
        pagination_class = None
        Produit.objects
     

class ProduitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =serializer.ProduitSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Produit.objects.filter(id=self.kwargs.get('pk' , None)) 
 
class ProspectListe(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        queryset = Prospect.objects.filter(delete = False)
        serializer_class =serializer.Prospecterializer
        pagination_class = None
        Prospect.objects
class ProspectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =serializer.Prospecterializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Prospect.objects.filter(id=self.kwargs.get('pk' , None)) 

class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =serializer.ContactSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Contact.objects.filter(id=self.kwargs.get('pk' , None)) 

class ContactListe(ListCreateAPIView):
        queryset = Contact.objects.filter(delete = False)
        permission_classes = [IsAuthenticated]
        pagination_class = None
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.ContactSerializer
                return serializer.RetriveContactSerializer 


class OpportunitiesListe(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True  ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.all().filter(delete=True ,user_id = self.request.user.id  ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeWinning(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True , phase='Gagnée'  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True , phase='Gagnée' ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.filter(delete=True , phase='Gagnée' ,user_id = self.request.user.id   ).order_by('creationDate')
       
        
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeNopa(ListCreateAPIView):
        
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True  ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.all().filter(delete=True ,user_id = self.request.user.id  ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeQualification(ListCreateAPIView):
        
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True , phase='Qualification'  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True , phase='Qualification' ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.filter(delete=True , phase='Qualification' ,user_id = self.request.user.id   ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer


class OpportunitiesListeEtude(ListCreateAPIView):
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True , phase='Etude de besoins'  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True , phase='Etude de besoins' ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.filter(delete=True , phase='Etude de besoins' ,user_id = self.request.user.id   ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeProposition(ListCreateAPIView):
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True , phase='Proposition commerciale'  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True , phase='Proposition commerciale' ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.filter(delete=True , phase='Proposition commerciale' ,user_id = self.request.user.id   ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer


class OpportunitiesListeNegociation(ListCreateAPIView):
      
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True , phase='Négociation'  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True , phase='Négociation' ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.filter(delete=True , phase='Négociation' ,user_id = self.request.user.id   ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListeGagnee(ListCreateAPIView):
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True , phase='Gagnée'  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True , phase='Gagnée' ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.filter(delete=True , phase='Gagnée' ,user_id = self.request.user.id   ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer

class OpportunitiesListePerdue(ListCreateAPIView):
        pagination_class = None
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return  Opportunities.objects.all().filter(delete=True , phase='Perdue'  ).order_by('creationDate')
                if self.request.user.role == 'manager':
                 return  Opportunities.objects.all().filter(delete=True , phase='Perdue' ).order_by('creationDate')
                if self.request.user.role == 'commerciale':
                 return  Opportunities.objects.filter(delete=True , phase='Perdue' ,user_id = self.request.user.id   ).order_by('creationDate')
        def get_serializer_class(self):
                if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
                return serializer.RetriveOpportunitiesSerializer


class OpportunitiesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =serializer.OpportunitiesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Opportunities.objects.filter(id=self.kwargs.get('pk' , None)) 

class ActionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =serializer.ActionSerializer 
    def get_queryset(self):
        return Action.objects.filter(id=self.kwargs.get('pk' , None)) 
class ProduitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =serializer.ProduitSerializer 
    def get_queryset(self):
        return Produit.objects.filter(id=self.kwargs.get('pk' , None)) 

class SumQualification1 (APIView) : 
        permission_classes = [IsAuthenticated]
        def get(self, request, format='json'):
         if request.method == 'GET':
                from django.db.models import Sum
                from api.models import Opportunities   

                # suma = Opportunities.objects.filter(phase='Qualification', delete=True).aggregate(Sum('estimatePrice'))
                if self.request.user.role == 'responsable':
                  suma =  Opportunities.objects.filter(delete=True , phase='Qualification'  ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'manager':
                  suma =  Opportunities.objects.filter(delete=True , phase='Qualification' ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'commerciale':
                 suma =  Opportunities.objects.filter(delete=True , phase='Qualification' ,user_id = self.request.user.id   ).aggregate(Sum('estimatePrice'))
                 return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
class SumEtude(APIView) : 
        permission_classes = [IsAuthenticated]
        def get(self, request, format='json'):
         if request.method == 'GET':
                from django.db.models import Sum
                from api.models import Opportunities   
            
                if self.request.user.role == 'responsable':
                  suma =  Opportunities.objects.filter(delete=True , phase='Etude de besoins'  ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'manager':
                  suma =  Opportunities.objects.filter(delete=True , phase='Etude de besoins' ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'commerciale':
                 suma =  Opportunities.objects.filter(delete=True , phase='Etude de besoins' ,user_id = self.request.user.id   ).aggregate(Sum('estimatePrice'))
                 return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })        
class Sumproposition(APIView) : 
        permission_classes = [IsAuthenticated]
        def get(self, request, format='json'):
         if request.method == 'GET':
                from django.db.models import Sum
                from api.models import Opportunities   
               
                if self.request.user.role == 'responsable':
                  suma =  Opportunities.objects.filter(delete=True , phase='Proposition commerciale'  ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'manager':
                  suma =  Opportunities.objects.filter(delete=True , phase='Proposition commerciale' ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'commerciale':
                 suma =  Opportunities.objects.filter(delete=True , phase='Proposition commerciale' ,user_id = self.request.user.id   ).aggregate(Sum('estimatePrice'))
                 return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })  
class SumNegociation(APIView) : 
        permission_classes = [IsAuthenticated]
        def get(self, request, format='json'):
         if request.method == 'GET':
                from django.db.models import Sum
                from api.models import Opportunities   
              
                if self.request.user.role == 'responsable':
                  suma =  Opportunities.objects.filter(delete=True , phase='Négociation'  ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'manager':
                  suma =  Opportunities.objects.filter(delete=True , phase='Négociation' ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'commerciale':
                 suma =  Opportunities.objects.filter(delete=True , phase='Négociation' ,user_id = self.request.user.id   ).aggregate(Sum('estimatePrice'))
                 return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })      

class SumGagnee(APIView) : 
        permission_classes = [IsAuthenticated]
        def get(self, request, format='json'):
         if request.method == 'GET':
                from django.db.models import Sum
                from api.models import Opportunities   
               
                if self.request.user.role == 'responsable':
                  suma =  Opportunities.objects.filter(delete=True , phase='Gagnée'  ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'manager':
                  suma =  Opportunities.objects.filter(delete=True , phase='Gagnée' ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'commerciale':
                 suma =  Opportunities.objects.filter(delete=True , phase='Gagnée' ,user_id = self.request.user.id   ).aggregate(Sum('estimatePrice'))
                 return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        }) 
class SumPerdu(APIView) : 
        permission_classes = [IsAuthenticated]
        def get(self, request, format='json'):
         if request.method == 'GET':
                from django.db.models import Sum
                from api.models import Opportunities   
                if self.request.user.role == 'responsable':
                  suma =  Opportunities.objects.filter(delete=True , phase='Perdue'  ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'manager':
                  suma =  Opportunities.objects.filter(delete=True , phase='Perdue' ).aggregate(Sum('estimatePrice'))
                  return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })
                if self.request.user.role == 'commerciale':
                 suma =  Opportunities.objects.filter(delete=True , phase='Perdue' ,user_id = self.request.user.id   ).aggregate(Sum('estimatePrice'))
                 return response.JsonResponse ( { 
                                'status' : True ,
                                'data' : suma['estimatePrice__sum'],
                                'message' : "worked"

                        })          
class OpportunityDetaills(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
                        return serializer.OpportunitiesSerializer
       
        return serializer.RetriveOpportunitiesSerializer
    def get_queryset(self): 
        return Opportunities.objects.filter(id=self.kwargs.get('pk' , None)) 

class ActionDetaills(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
                        return serializer.ActionSerializer
        return serializer.RetriveActionbbbbSerializer
    def get_queryset(self): 
        return Action.objects.filter(id=self.kwargs.get('pk' , None))  

class ContactDetaills(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
                        return serializer.ContactSerializer
        return serializer.RetriveContactSerializer
    def get_queryset(self): 
        return Contact.objects.filter(id=self.kwargs.get('pk' , None))  

        
class ProcpectDetaills(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
                        return serializer.Prospecterializer
        return serializer.Prospecterializer
    def get_queryset(self): 
        return Prospect.objects.filter(id=self.kwargs.get('pk' , None))  


class ProduitDetaills(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
                        return serializer.ProduitSerializer
        return serializer.ProduitSerializer
    def get_queryset(self): 
        return Produit.objects.filter(id=self.kwargs.get('pk' , None))  

class emailListe(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        pagination_class = None
        def get_serializer_class(self):
                if self.request.method == 'POST':
                                return serializer.ActionSerializer
        
                return serializer.RetriveActionbbbbSerializer
        
        def get_queryset(self): 
       
                return Action.objects.all().filter(type='email' , Opportunity_id= self.kwargs.get('pk' , None)  )
       
class callListe(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        # serializer_class =serializer.RetriveActionbbbbSerializer
        pagination_class = None
        def get_serializer_class(self):
                if self.request.method == 'POST':
                                return serializer.ActionSerializer
        
                return serializer.RetriveActionbbbbSerializer
        # def get_queryset(self):
        #         return Contact.objects.all()
        def get_queryset(self): 
       
                return Action.objects.all().filter(type='phone call' , Opportunity_id= self.kwargs.get('pk' , None)  )
       
class meetingListe(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        # serializer_class =serializer.RetriveActionbbbbSerializer
        pagination_class = None
        def get_serializer_class(self):
                if self.request.method == 'POST':
                                return serializer.ActionSerializer
        
                return serializer.RetriveActionbbbbSerializer
        
        def get_queryset(self): 
       
                return Action.objects.all().filter(type='meeting' , Opportunity_id= self.kwargs.get('pk' , None)  )
       
                       
class ActionListe(ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class =serializer.ActionSerializer
        pagination_class = None
        def get_queryset(self):
                if self.request.user.role == 'responsable':
                  return   Action.objects  .all()
                if self.request.user.role == 'manager':
                 return  Action.objects.all()
                if self.request.user.role == 'commerciale':
                 return Action.objects.filter(user_id = self.request.user.id   )
           


class UserLogged(ListCreateAPIView) : 
	permission_classes = [IsAuthenticated]
        # def get_queryset(self):
        #     queryset = super(UserLocationsListView , self).get_queryset()
        #     queryset = queryset.filter(user=self.request.user)
        #     return queryset
	def get(self, request, format='json'):
                if request.method == 'GET':
	        
                        if request.user.is_authenticated :
                               
                                        return response.JsonResponse ( { 
                                                        'status' : True ,
                                                        'data' : [ request.user.email, request.user.nom , request.user.prenom , request.user.role ] ,
                                                        'message' : "worked"

                                                })  
                        
