from django.contrib import admin
from .models import *
# Register your models here.

class subscriberadmin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for  field in subscriber._meta.fields]
    list_filter = ["username", ]
    search_fields = ["username", "email","tel",]
    #inlines= []
    #fields = [""]
    #exclude = ["comm"]
    empty_value_display = '-empty-'

    class Meta:
        model = subscriber

admin.site.register(subscriber, subscriberadmin)
