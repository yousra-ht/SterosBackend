

from django.contrib.auth.models import User
from django.http import response
from CRMBackend.permissions import AuthorAllStaffAllButEditOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import NewUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import  RegisterSerializer, UserImageSerializer, UserSerializer 

import base64 , os

class Register(APIView):
	
	permission_classes = [IsAuthenticated ]


	def post(self, request, format='json'):
		
			if request.method == 'POST':
					data = {}
					email = request.data.get('email', '0').lower()
					if validate_email(email) != None:
							data['error_message'] = 'That email is already in use.'
							data['response'] = 'Error'
							return Response(data,status=status.HTTP_400_BAD_REQUEST)
					serializer = RegisterSerializer (data=request.data)
					
					if serializer.is_valid():
						user = serializer.save()
						if user:
							json = serializer.data
							return Response(json, status=status.HTTP_201_CREATED)
					return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def validate_email(email):
			user = None
			try:
				  user =  NewUser.objects.get(email=email)
			except  NewUser.DoesNotExist:
				return None
			if user != None:
				return email


class ListeOfUser(ListCreateAPIView):

	permission_classes = [IsAuthenticated]
	queryset = NewUser.objects.all()
	serializer_class = UserSerializer

	# def get_queryset(self):
	# 	queryset = NewUser.objects.all()
	# 	for user in queryset :
	# 		    if  user.email: 
	# 							return user.email
				# image_format = os.path.splitext(user.image)[-1].replace('.', '').lower()
				# encoded_string = base64.b64encode(image_data).decode('utf-8')

				# if image_format in ['jpg', 'jpeg', 'png', 'gif']:
				# 	image =  'data:image/%s;base64,%s' % (image_format, encoded_string)
	NewUser.objects


class ListeOfUserWithoutpagination(ListCreateAPIView):

	permission_classes = [IsAuthenticated]
	queryset = NewUser.objects.all()
	serializer_class = UserSerializer
	pagination_class = None
	NewUser.objects

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return NewUser.objects.filter(id=self.kwargs.get('pk' , None)) 

class Images(ListCreateAPIView) : 
		
    serializer_class =UserImageSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return NewUser.objects.filter(id=self.kwargs.get('pk' , None)) 

