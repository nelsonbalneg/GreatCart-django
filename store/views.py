from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request, category_slug = None):
    #retrieve products by category
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
        product_count = products.count()
    else:
         #query to retrieve all the available products
        products = Product.objects.all().filter(is_available = True)

        #query to count all the products
        product_count = Product.objects.all().filter(is_available = True).count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    #get the details of a single product
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    #create a context dictionary and pass it to the template
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)