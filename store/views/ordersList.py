from django.views import View
from django.shortcuts import render
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from store.models.orders import Order

class Order_List(View):

    @method_decorator(auth_middleware)
    def get(self, request):

        customer = request.session.get('customer')
        data = Order.all_orders_by_customer(customer)
        for i in data:
            print(i.id)
        return render(request, 'ordersList.html', {'orderListData': data})