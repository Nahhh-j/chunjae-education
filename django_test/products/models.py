from django.db import models

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name