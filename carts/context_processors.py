from carts.models import CartItem,Cart
from carts.views import _cart_id

# this is context processor which we are using in the directly links
def counter(request):
    cart_count=0
    if 'admin'  in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            
            cart_items=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count=0
    print(cart_count)
    return dict(cart_count=cart_count)