from django.contrib import admin
from .models import *
# Register your models here.

class suppliers_admin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for  field in supplier._meta.fields]
    list_filter = ["sup_name", ]
    search_fields = ["sup_name", "sup_address","sup_cont",]
    #inlines= []
    #fields = [""]
    #exclude = ["comm"]
    empty_value_display = '-empty-'

    class Meta:
        model = supplier

admin.site.register(supplier, suppliers_admin)

