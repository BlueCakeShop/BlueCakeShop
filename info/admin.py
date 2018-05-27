from django.contrib import admin
from .models import *
# Register your models here.

class info_admin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for  field in info._meta.fields]
    list_filter = ["user_name", "question_theme", "created",]
    search_fields = ["last_name", "email","tel",]
    #inlines= []
    #fields = [""]
    #exclude = ["comm"]
    empty_value_display = '-empty-'

    class Meta:
        model = info

admin.site.register(info, info_admin)

