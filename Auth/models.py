from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class AccountManager(BaseUserManager):
    def create_superuser(self, email,  nom , prenom,password, image , role , phone ,Tel,Fax ,Ville ,adresse , description, birthday ,pays ,Color , **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, nom , prenom, image , password,phone ,  role ,Tel,Fax ,Ville ,adresse , description, birthday ,pays ,Color , **other_fields)
    def create_user(self, email,  nom , prenom, image , role , phone ,Tel,Fax ,Ville ,adresse , description, birthday ,pays , password,Color , **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, 
                          prenom=prenom,
                          role=role, 
                          nom=nom ,
                          phone=phone, 
                          Tel=Tel,
                          Fax=Fax , 
                          Ville=Ville,
                          adresse =adresse,
                          description =description ,
                          birthday =birthday ,
                          pays = pays,
                          Color =Color 
                          ,**other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    image =  models.ImageField(upload_to='images' )
    role =  models.CharField(max_length=150, blank=True)
    nom = models.CharField(max_length=150, blank=True)
    prenom= models.CharField(max_length=150, blank=True)
    Tel= models.CharField(max_length=150, blank=True)
    Fax =  models.CharField(max_length=150, blank=True)
    Ville = models.CharField(blank=True, max_length=150)
    adresse= models.CharField(blank=True, max_length=150)
    description =models.TextField(blank=True, null=True)
    pays =models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=150)
    birthday =models.CharField(blank=True, max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    Color = models.CharField(blank=True, max_length=150)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
   
    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom' , 'prenom' , 'role']
  