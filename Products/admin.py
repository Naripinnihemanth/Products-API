from django.contrib import admin
from .models import *
class productAdmin(admin.ModelAdmin):
    list_display=("id","title","category")

admin.site.register(productModel,productAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=("id","categories")

admin.site.register(categoryModel,categoryAdmin)