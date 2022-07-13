import re
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from store.features.email import Email
import time

class Signup(View):

    def register_user(self, request):
        message = ""
        post_data = request.POST
        first_name = post_data.get('fname')
        last_name = post_data.get('lname')
        email = post_data.get('email')
        password = make_password(post_data.get('password'))
        phone = post_data.get('phone')
        try:
            if Customer.customer_by_email_id(email):
                message = "Email Address Already Registered"
                return render(request, 'signup.html', {'message': message})
            
        except:
            request.session['otp'] = "1234"
            request.session['signup_info'] =   {
                'first_name':first_name, 
                'last_name':last_name, 
                'email':email, 
                'password':password, 
                'phone_number':phone
            }
            
            print(request.session.get('otp'))
            print(request.session.get('signup_info'))
            Email.send_otp_to_email(request, email)
            return render(request, 'otpVerification.html')
            

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        return self.register_user(request)