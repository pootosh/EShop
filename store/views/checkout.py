from django.views import View
from django.shortcuts import render, redirect
from store.models.orders import Order
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Checkout(View):

    def get(self, request):
        return redirect('cart')

    @method_decorator(auth_middleware)
    def post(self, request):
        customer_id = request.session.get('customer')
        customer = Customer(id=customer_id)
        cart = request.session.get('cart')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        total = request.POST.get('totalPrice')
        print(customer,"        ", cart, address, phone)
        order = Order(
            customer=customer,
            cart=cart,
            address=address,
            phone=phone,
            order_total = total
        )

        order.order_place()
        request.session['cart'] = {}
        return redirect('cart')