from api import views
from django.conf import urls
from django.urls import path

urlpatterns = [
    path('products', views.ProduitListe.as_view() ),
    path('prospects', views.ProspectListe.as_view() ),
    path('Contact', views.ContactListe.as_view() ),
    path('Allopportunities/', views.OpportunitiesListe.as_view() ),
    path('WinnningOpportunities/', views.OpportunitiesListeWinning.as_view() ),
    path('<int:pk>', views.ProduitRetrieveUpdateDestroyAPIView.as_view()), 
    path('AllopportunitiesNopa/', views.OpportunitiesListeNopa.as_view() ),
     path('opportunitiesQualification/', views.OpportunitiesListeQualification.as_view() ),
    path('opportunitiesEtude/', views.OpportunitiesListeEtude.as_view() ),
    path('opportunitiesProposition/', views.OpportunitiesListeProposition.as_view() ),
    path('opportunitiesNegociation/', views.OpportunitiesListeNegociation.as_view() ),
    path('opportunitiesGagnee/', views.OpportunitiesListeGagnee.as_view() ),
    path('opportunitiesPerdue/', views.OpportunitiesListePerdue.as_view() ),
    path('Updateopportunities/<int:pk>', views.OpportunitiesRetrieveUpdateDestroyAPIView.as_view() ),
    path('opportunityDetaills/<int:pk>', views.OpportunityDetaills.as_view() ),
    path('emailListe/<int:pk>', views.emailListe.as_view() ),
    path('callListe/<int:pk>', views.callListe.as_view() ),
    path('meetingListe/<int:pk>', views.meetingListe.as_view() ),
    path('ActionListe/', views.ActionListe.as_view() ),
    path('SumQualification/', views.SumQualification ),
    # path('^Opportunity/(?P<username>.+)/$', PurchaseList.as_view()),
]