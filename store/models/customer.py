from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=10)

    def register(self):
        self.save()

    @staticmethod
    def customer_by_email_id(email):
        return Customer.objects.get(email=email)