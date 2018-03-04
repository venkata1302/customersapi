from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)


class Products(models.Model):
    company_name = models.CharField(max_length=20)
    product_type = models.CharField(max_length = 20)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)



