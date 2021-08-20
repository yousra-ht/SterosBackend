from Auth.views import ListeOfUser, ListeOfUserWithoutpagination
from Auth.views import Register
from django.conf import urls
from django.urls import path
from rest_framework_simplejwt.views  import (
     TokenObtainPairView,
     TokenRefreshView,
     TokenVerifyView,
   )

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', Register.as_view(), name='register'),
    path('Users/', ListeOfUser.as_view(), name='Users'),
    path('UsersNOpag/', ListeOfUserWithoutpagination.as_view(), name='register'),

]