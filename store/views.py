from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category
# Create your views here.
def store(request,category_slug=None):
    categories=None,
    product=None
    if category_slug!=None: #this specific ath is for the searching specif item as shirt in our datase and it shows it only
        categories=get_object_or_404(Category,slug=category_slug)
        product=Product.objects.filter(category=categories,is_available=True) #this is used to make filter for the Product models check the category and show that only category
        product_count=product.count()
    else:
        product = Product.objects.all().filter(is_available=True)
        product_count=product.count()
    context={
        'products':product,
        'products_count':product_count
    }
    return render(request, 'store/store.html',context)


def product_detail(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    context={
        'single_product':single_product,    
    }
    return render(request,'store/product_details.html',context)