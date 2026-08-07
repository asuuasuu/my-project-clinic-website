from django.db import models
from django.utils.text import slugify


class Category(models.Model):
      name = models.CharField(max_length = 100, unique = True, blank = False)

      slug = models.CharField(max_length = 100, unique = True, blank = True)
      #автоматично генерує slug за допомогою slugify
      #якщо нічого в blank не написано
      def save(self, *args, **kwargs):
            if not self.slug:
                  self.slug = slugify(self.name)
            super().save(*args, **kwargs)

      def __str__(self):
          return self.name


class Product(models.Model):
      name = models.CharField(max_length = 100, blank = False)
      category = models.ForeignKey(Category, blank = False, on_delete = models.CASCADE)
      price = models.DecimalField(max_digits = 10, decimal_places = 2)
      description = models.TextField(blank = False, default='')
      main_product_image = models.ImageField(blank = False, upload_to = 'product/main/')
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      ingredients = models.TextField(blank = False, default='')
      slug = models.CharField(max_length = 100, unique = True, blank = True)
      quantity = models.PositiveIntegerField(default = 0)

      def save(self, *args, **kwargs):
            if not self.slug:
                  self.slug = slugify(self.name)
            super().save(*args, **kwargs)

      def __str__(self):
          return self.name


class ProductImage(models.Model):
      product = models.ForeignKey(Product, blank = False, on_delete = models.CASCADE)
      extra_image = models.ImageField(upload_to = 'product/extra/')
