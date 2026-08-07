from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInLine(admin.TabularInline):
      model = ProductImage
      extra = 0
      max_num = 6


class ProductAdmin(admin.ModelAdmin):
      list_display = ['category', 'name', 'price', 'created_at', 'updated_at', 'quantity']

      search_fields = ['name', 'category', 'quantity']

      prepopulated_fields = {'slug': ('name',)}

      inlines = [ProductImageInLine]


class CategoryAdmin(admin.ModelAdmin):
      list_display = ['name']

      search_fields = ['name']

      prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
