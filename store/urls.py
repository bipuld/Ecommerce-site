from django.urls import path,include
from store import views
urlpatterns = [

    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='products_by_category'), #this is for the specific path searh like as shirt it show shirt item only
    path('<slug:category_slug>/<slug:product_slug>',views.product_detail,name='product_details')
]
