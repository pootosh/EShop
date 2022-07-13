from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Index(View):
    def get(self, request):
        products = None
        categories = Category.get_all_category()
        data = {}
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_products_by_category_id(category_id)
        else:
            products = Product.get_all_products()
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove_product = request.POST.get('remove_product')
        if cart:
            if product in cart:
                if remove_product:
                    cart[product] -= 1
                    if cart[product] ==0:
                        cart.pop(product)
                else:
                    cart[product] += 1
            else:
                cart[product]=1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('home')

