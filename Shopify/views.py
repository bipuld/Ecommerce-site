from django.shortcuts import render,redirect
from store.models import Product

def home(request):
    product=Product.objects.all().filter(is_available=True)
    context={
        
    'products':product
    }
    return render(request,'home.html',context)