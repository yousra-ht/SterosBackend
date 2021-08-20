from django.contrib import admin
from .models import NewUser
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email','role',  'prenom','image','nom','id' )
    list_filter = ('email','role' ,'prenom','nom', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'prenom','nom','role',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email',  'prenom','nom' , 'role' , 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'prenom','nom','role','image', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)