from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from . models import *
from . forms import *


from cart.forms import CartAddProductForm


# Create your views here.

def product_list(request, category_slug=None):
    products = Product.objects.filter(product_is_active=True)
    prod_photos = Product_photo.objects.filter(product_photo_is_main=True, product_photo_is_active=True)
    return render(request, 'products/list.html', locals())



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, product_slug=slug, product_is_active=True)
    product_photos = Product_photo.objects.filter(product = product, product_photo_is_active=True )
    comments = Product_comments.objects.filter(pc_product__pk = id)
    comment_form = pc_form(request.POST or None)
    cart_product_form = CartAddProductForm()
    if request.method == "POST":
        comment_form = pc_form(request.POST, request.FILES)
        if comment_form.is_valid():
            new_form = comment_form.save(commit = False)
            new_form.pc_product = product
            # new_pc_photo = comment_form.cleaned_data['pc_photo']
            new_form.save()
            comment_form = pc_form()
            messages.success(request, 'Ваш отзыв отправлен!')
            return HttpResponseRedirect('')
        else:
            comment_form = pc_form()
    return render(request,'products/product_det.html', locals())
