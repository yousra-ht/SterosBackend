from rest_framework import serializers 
from .models import  NewUser
from rest_framework.response import Response

class RegisterSerializer(serializers.ModelSerializer):
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace', 'patch']
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = NewUser
        fields = ('email',  'password' , 'password2' , 'nom','prenom' , 'image' , 'role' , 'phone'  ,'Tel','Fax' ,'Ville' ,'adresse' , 'description', 'birthday' ,'pays' , "Color", 'delete')
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
    image = serializers.ImageField(
            max_length=None, use_url=False
        )
    class Meta:
        model = NewUser
        fields = "__all__"
    # def update(self, *args, **kwargs ):

            # user = super().update(*args ,**kwargs)
           
            # if user.password != validated_data.pop('password2', None):
                    
            #         raise serializers.ValidationError({'password': 'Passwords must match !!.'})
            # else :
            # p = user.password
            # user.set_password(p)
            # user.save()
            # return user


  
        
class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('image' ,)


class UserForPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = NewUser
        fields =('password' , 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    def update(self, *args, **kwargs ):

            user = super().update(*args ,**kwargs)
           
            # if user.password != validated_data.pop('password2', None):
                    
            #         raise serializers.ValidationError({'password': 'Passwords must match !!.'})
            # else :
            p = user.password
            user.set_password(p)
            user.save()
            return user

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = NewUser
        fields = ('email', 'nom','prenom'  , 'role' , 'phone'  ,'Tel' ,'Ville' ,'adresse' , 'birthday' ,'pays' , "Color")
     

    def validate_email(self, value):
        user = self.context['request'].user
        if NewUser.objects.exclude(pk=user.pk).filter(email=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError( {"This email is already in use ops."})
        return value

 
    def partial_update(self, instance, validated_data ,**kwargs ):
        kwargs['partial'] = True
        instance.nom = validated_data['nom']
        instance.prenom = validated_data['prenom']
        instance.email = validated_data['email']
        # instance.image = validated_data['image']

        instance.role = validated_data['role']
        instance.phone = validated_data['phone']
        instance.Tel = validated_data['Tel']
        instance.Ville = validated_data['Ville']

        instance.adresse = validated_data['adresse']
        instance.birthday = validated_data['birthday']
        instance.pays = validated_data['pays']
        instance.Color = validated_data['Color']

        instance.save()

        return instance