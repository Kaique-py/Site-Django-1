from django.contrib import admin

# Register your models here.
from .models import Categoria, Item

admin.site.register(Categoria)
admin.site.register(Item)