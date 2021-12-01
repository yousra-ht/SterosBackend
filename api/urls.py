from api import views
from django.conf import urls
from django.urls import path


urlpatterns = [
    path('products', views.ProduitListe.as_view() ),
    path('TypeProduit', views.TypeProduitListe.as_view() ),
    path('TypeProduitDetaills/<int:pk>', views.TypeProduitDetaills.as_view() ),

    path('UpdateTypeProduit/<int:pk>', views.TypeProduitRetrieveUpdateDestroyAPIView.as_view() ),
    path('prospects', views.ProspectListe.as_view() ),
    path('Contact', views.ContactListe.as_view() ),
    path('Allopportunities/', views.OpportunitiesListe.as_view() ),
    path('WinnningOpportunities/', views.OpportunitiesListeWinning.as_view() ),
    path('AllopportunitiesNopa/', views.OpportunitiesListeNopa.as_view() ),
     path('opportunitiesQualification/', views.OpportunitiesListeQualification.as_view() ),
    path('opportunitiesEtude/', views.OpportunitiesListeEtude.as_view() ),
    path('opportunitiesProposition/', views.OpportunitiesListeProposition.as_view() ),
    path('opportunitiesNegociation/', views.OpportunitiesListeNegociation.as_view() ),
    path('opportunitiesGagnee/', views.OpportunitiesListeGagnee.as_view() ),
    path('opportunitiesPerdue/', views.OpportunitiesListePerdue.as_view() ), 
     path('OpportunitiesListeGagneeNopa/', views.OpportunitiesListeGagneeNopa.as_view() ), 
    path('Updateopportunities/<int:pk>', views.OpportunitiesRetrieveUpdateDestroyAPIView.as_view() ),
    path('UpdateAction/<int:pk>', views.ActionRetrieveUpdateDestroyAPIView.as_view() ),
    path('UpdateProduit/<int:pk>', views.ProduitRetrieveUpdateDestroyAPIView.as_view() ),
    path('opportunityDetaills/<int:pk>', views.OpportunityDetaills.as_view() ),
    path('emailListe/<int:pk>', views.emailListe.as_view() ),
    path('callListe/<int:pk>', views.callListe.as_view() ),
    path('meetingListe/<int:pk>', views.meetingListe.as_view() ),
    path('ActionListe/', views.ActionListe.as_view() ),
    path('sumQualification/', views.SumQualification1.as_view() ),
    path('sumEtude/', views.SumEtude.as_view() ),
    path('Sumproposition/', views.Sumproposition.as_view() ),
    path('SumNegociation/', views.SumNegociation.as_view() ),
    path('SumGagnee/', views.SumGagnee.as_view() ),
    path('SumPerdu/', views.SumPerdu.as_view() ),
    path('UserLogged/', views.UserLogged.as_view() ),
    path('ActionDetaills/<int:pk>', views.ActionDetaills.as_view() ),
    path('ProduitDetaills/<int:pk>', views.ProduitDetaills.as_view() ),
    path('ProspectDetaills/<int:pk>', views.ProcpectDetaills.as_view() ),
    path('UpdateProspect/<int:pk>', views.ProspectRetrieveUpdateDestroyAPIView.as_view() ),
    path('ContactDetaills/<int:pk>', views.ContactDetaills.as_view() ),
    path('UpdateContact/<int:pk>', views.ContactRetrieveUpdateDestroyAPIView.as_view() ),
    path('UserLogged',  views.UserLogged.as_view()),
    path('UpdateVille/<int:pk>',  views.VilletRetrieveUpdateDestroyAPIView.as_view()),
    path('villeListe',  views.VilleListe.as_view()),
    path('villeDetaills/<int:pk>', views.VilleDetaills.as_view() ),

    path('paysListe',  views.PaysListe.as_view()),


    path('LangueListe',  views.LangueListe.as_view()),
    path('langueDetaills/<int:pk>', views.LangueDetaills.as_view() ),
    path('UpdateLangue/<int:pk>',  views.LanguetRetrieveUpdateDestroyAPIView.as_view()),

    path('Paysdetaills/<int:pk>',  views.PaysDetaills.as_view()),
    path('UpdatePays/<int:pk>',  views.PaystRetrieveUpdateDestroyAPIView.as_view()),
    path('competitionListe/<int:pk>',  views.competitionListe.as_view()),
    path('updateCompte/<int:pk>', views.competitiontRetrieveUpdateDestroyAPIView.as_view() ),
    path('competitionListeAdd',  views.competitionListeADD.as_view()),
    path('competitionDetaills/<int:pk>',  views.competitionDetaills.as_view()),
    path('ContactOfProdpect/<int:pk>', views.ContactofProspect.as_view() ),
    path('ActionOpportunity/<int:pk>', views.ActionListeOpportunity.as_view() ),
    path('VilleofPays/<int:pk>', views.VilleListePays.as_view() ),
    path('Goalsliste/<int:pk>', views.GoalsListe.as_view() ),

]