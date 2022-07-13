from decimal import DecimalException
from http.client import ACCEPTED
from os import stat
from telnetlib import STATUS
from django.db import models
from .customer import Customer
from django.utils import timezone

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING'
        DECLINED = 'DECLINED'
        ACCEPTED = 'ACCEPTED'
        DELIVERED = 'DELIVERED'

    customer = models.ForeignKey(Customer, default=None, on_delete=models.CASCADE)
    cart = models.JSONField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    order_total = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=25, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    

    def order_place(self):
        self.save()

    @staticmethod
    def all_orders_by_customer(customer):
        return Order.objects.filter(customer=customer).order_by('-id')