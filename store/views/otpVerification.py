from django.shortcuts import redirect, render
from django.views import View
from store.models import Customer

class Verify(View):
    def post(self, request):
        otp = request.POST.get('otp')
        print(otp, type(otp))
        if int(otp) ==int(request.session.get('otp')):
            user = request.session.get('signup_info')
            customer = Customer(
                first_name=user['first_name'], 
                last_name=user['last_name'], 
                email=user['email'], 
                password=user['password'], 
                phone_number=user['phone_number']
            )
            customer.register()
            return redirect('login')
        else:
            message = "Incorrect Otp"
            return render(request, 'signup.html', {'message': message})