from django.contrib import admin
from .models import Action, Contact, Opportunities, Produit, Prospect

admin.site.register(Action)
admin.site.register(Produit)
admin.site.register(Prospect)
admin.site.register(Contact)
admin.site.register(Opportunities)

