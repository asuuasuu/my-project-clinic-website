from django.contrib import admin
from .models import CartItem

class CartItemAdmin(admin.ModelAdmin):
      list_display = ['date_added', 'product', 'quantity']

admin.site.register(CartItem, CartItemAdmin)
