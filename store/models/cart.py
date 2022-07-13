from os import stat
from django.db import models
from .customer import Customer

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    items = models.JSONField(null=True)

    def register(self):
        self.save()

    @staticmethod
    def cart_by_id(customer):
        return Cart.objects.get(customer=customer).id
