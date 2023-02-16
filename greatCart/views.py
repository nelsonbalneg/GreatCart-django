from django.shortcuts import render
from store.models import Product

def home(request):
    #query to retrieve all the products
    products = Product.objects.all().filter(is_available = True)

    context = {
        'products': products,
    }
    return render(request,'home.html',context)