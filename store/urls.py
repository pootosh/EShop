from django.contrib import admin
from django.urls import path
from .views import home
from .views import signup
from .views import login
from .views import cart
from .views import checkout
from .views import ordersList
from .views import otpVerification

urlpatterns = [
    path('', home.Index.as_view(), name='home'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout', checkout.Checkout.as_view(), name='checkout'),
    path('ordersList', ordersList.Order_List.as_view(), name='ordersList'),
    path('otpVerification',otpVerification.Verify.as_view(), name='otpVerification'),
]
