from django.shortcuts import render
from .models import Product


def store(request):

    return render(request, 'store.html')


def product_detail(request,category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        'single_product': single_product
    }
   
    return render(request, 'product_detail.html',context)