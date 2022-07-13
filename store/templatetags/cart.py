from django import template
from store.models.product import Product
register = template.Library()

@register.filter(name='product_in_cart')
def product_in_cart(product, cart):
    new_cart = {str(i):cart[i] for i in cart}
    if str(product.id) in new_cart:
        if new_cart[str(product.id)]==0:
            return False
        return True
    else:
        return False

@register.filter(name='quantity_in_cart')
def quantity_in_cart(product, cart):
    return cart[str(product.id)]

@register.filter(name='cart_products')
def cart_products(product, cart):
    if cart[str(product.id)]>0:
        return True
    else:
        False

@register.filter(name='product_total')
def product_total(product, cart):
    return cart[str(product.id)]*product.price

@register.filter(name='total_price')
def total_price(products, cart):
    total = 0
    for product in products:
        total+=product_total(product, cart)
    return total

