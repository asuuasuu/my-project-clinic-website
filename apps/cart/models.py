from django.db import models
from apps.product.models import Product

class CartItem(models.Model):
      product = models.ForeignKey(Product, on_delete = models.CASCADE)
      quantity = models.PositiveIntegerField(Product, default = 0)
      date_added = models.DateTimeField(auto_now_add = True)

      def __str__(self):
            return f'{self.quantity} x {self.product.name}'
      