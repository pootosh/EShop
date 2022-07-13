from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.cart import Cart
from django.views import View

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    
    def post(self, request):
        print("url: ",self.return_url)
        message = ""
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:      
            user = Customer.customer_by_email_id(email)
            if check_password(password, user.password):
                request.session['customer'] = user.id
                request.session['email'] = user.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                return redirect('home')
            else:
                message = 'Incorrect Password'
            
        except:
            message = 'Invalid Credentials'
        return render(request,'login.html',{'message': message})

def logout(request):
    
    customer = Customer.customer_by_email_id(request.session.get('email'))
    items = request.session.get('cart')
    try:
        cart_id = Cart.cart_by_id(customer)
        cart = Cart.objects.get(id = cart_id)
        if items==None:
            cart.items = {}
            cart.save()
        else:
            cart.items = items
            cart.save()
    except:
        print(2)
        cart = Cart(
            customer = customer,
            items = items
        )
        cart.register()
    print(items)
    request.session.clear()
    return redirect('home')