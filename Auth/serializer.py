from rest_framework import serializers 
from .models import  NewUser

class RegisterSerializer(serializers.ModelSerializer):
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace']
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = NewUser
        fields = ('email',  'password' , 'password2' , 'nom','prenom' , 'image' , 'role')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
		    password  = validated_data.pop('password', None)
		    password2 = validated_data.pop('password2', None)
	
		    instance = self.Meta.model(**validated_data)
		    if password != password2:
			      
			      raise serializers.ValidationError({'password': 'Passwords must match !!.'})
		    else :
				   instance.set_password(password)
		       
		    instance.save()
		    return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"