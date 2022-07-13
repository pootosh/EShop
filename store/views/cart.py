from django.views import View
from django.shortcuts import render, redirect
from store.models import product

class Cart(View):
    def get(self, request):
        products = []
        if 'cart' not in dict(request.session):
            request.session['cart']={}
        try:
            ids = list(request.session.get('cart').keys())
            products = product.Product.get_all_products_by_id(ids)
            
        except:
            pass
        return render(request, 'cart.html', {'products': products})

    