from os import stat
from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to="uploads/products/")

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        return Product.objects.filter(category = category_id)

    @staticmethod
    def get_all_products_by_id(ids):
        return Product.objects.filter(id__in = ids)
