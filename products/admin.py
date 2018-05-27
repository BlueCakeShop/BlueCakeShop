from django.contrib import admin
from .models import *

from django.template.defaultfilters import truncatewords

# Register your models here.

class Product_photo_Inline(admin.TabularInline):
    model = Product_photo
    extra = 1

# class Category_photo_Inline(admin.TabularInline):
#     model = Category_photo
#     extra = 1

# class Category_admin(admin.ModelAdmin):
#     list_display = ['category_name', 'category_slug']
#     prepopulated_fields = {'category_slug': ('category_name', )}
#     inlines =[Category_photo_Inline]
#     class Meta:
#         model = Category
# admin.site.register(Category, Category_admin)

# class Category_photo_admin(admin.ModelAdmin):
#     list_display = [field.name for field in Category_photo._meta.fields]
#
#     #list_filter = ["name", ]
#     #search_fields = ["name"]
#     # #fields = [""]
#     # #exclude = ["comm"]
#     class Meta:
#         model = Category
# # admin.site.register(Category_photo, Category_photo_admin)


class Product_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields if field.name != 'product_description']
    list_filter = ['product_name', 'product_price', 'product_updated',]
    list_editable = ['product_price', 'product_stock', 'product_is_active']
    search_fields = ['product_name']
    inlines =[Product_photo_Inline]
    prepopulated_fields = {'product_slug': ('product_name', )}
    # #fields = [""]
    # exclude = ["product_description"]
    class Meta:
        model = Product
admin.site.register(Product, Product_admin)



class Product_photo_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product_photo._meta.fields]

    class Meta:
        model = Product
# admin.site.register(Product_photo, Product_photo_admin)


class Product_comments_admin(admin.ModelAdmin):
    list_display = [field.name for field in Product_comments._meta.fields]
    # list_display = [field.name for  field in subscriber._meta.fields]
    list_filter = ["pc_product", "pc_created", "pc_updated", "pc_replied", ]
    search_fields = ["pc_product", "pc_user_name"]
    # inlines =[]
    # fields = [""]
    # exclude = ["product_description"]
    class Meta:
        model = Product_comments
admin.site.register(Product_comments, Product_comments_admin)
