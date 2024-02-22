from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category
from carts.models import Cart,CartItem
from carts.views import _cart_id
from django.shortcuts import HttpResponse
# Create your views here.
def store(request,category_slug=None):
    categories=None,
    product=None
    if category_slug!=None: #this specific ath is for the searching specif item as shirt in our datase and it shows it only
        categories=get_object_or_404(Category,slug=category_slug)
        print(categories)
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
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request)) #this is cart__car_id go to model cart and cart_id attribute
        # return HttpResponse(in_cart) this in_cart function is used to check if that is already added in acart it says view or continue in product detail page win secific prduct

    except Exception as e:
        raise e
    context={
        'single_product':single_product,    
        'in_cart':in_cart,
    }
    return render(request,'store/product_details.html',context)