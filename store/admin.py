from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.cart import Cart
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'description','category', 'price', 'description']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'password']

class CustomerCart(admin.ModelAdmin):
    list_display = ['customer', 'items']
# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Cart, CustomerCart)
admin.site.register(Order)
