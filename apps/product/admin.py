from django.contrib import admin
from .models import Category, Product, ProductImage

class ProductImageInLine(admin.TabularInline):
      model = ProductImage
      extra = 5
      max_num = 5

class ProductAdmin(admin.ModelAdmin):
      list_display = ['category', 'name', 'price']

      search_fields = ['name', 'category']

      prepopulated_fields = {'slug': ('name',)}

      inlines = [ProductImageInLine]

class CategoryAdmin(admin.ModelAdmin):
      list_display = ['name']

      search_fields = ['name']

      prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
