from django.conf import settings
from django.conf.urls.static import static



from Auth.views import Images, ListeOfUser, ListeOfUserWithoutpagination, UserCHangePassword  , UserRetrieveUpdateDestroyAPIView, UserUpdateDestroyAPIView
from Auth.views import Register

from django.urls import path
from rest_framework_simplejwt.views  import (
     TokenObtainPairView,
     TokenRefreshView,
     TokenVerifyView,
   )




urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', Register.as_view(), name='register'),
    path('userdetaills/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view() ),
    path('Users/', ListeOfUser.as_view(), name='Users'),
    path('UsersNOpag/', ListeOfUserWithoutpagination.as_view(), name='register'),
    path('image/<int:pk>', Images.as_view() ),

    path('UpdatePasswordUser/<int:pk>', UserCHangePassword.as_view() ),
    path('UpdateUser/<int:pk>', UserUpdateDestroyAPIView.as_view() ),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)