from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=150, unique = True)
    slug = models.SlugField(max_length=150, unique = True)
    description = models.CharField(max_length=150, blank = True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)
    # cascade - When the referenced object is deleted, also delete the objects that have references to it.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)
    
    # url for the products
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    
    def __str__(self):
        return self.product_name