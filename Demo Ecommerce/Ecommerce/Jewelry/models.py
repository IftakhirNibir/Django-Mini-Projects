from django.db import models
from django.contrib.auth.models import User
import uuid

class MainCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'MainCategories'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    main_category = models.ForeignKey(MainCategory, related_name='mitems', on_delete=models.CASCADE)
    sub_categories = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True)
    purity = models.CharField(max_length=255, blank=True)  # For gold earrings
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True)  # For gold earrings
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    thumnail_image = models.ImageField(upload_to='item_images', blank=True, null=True)
    images =  models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    total_ordered_quantity = models.IntegerField(default=0)  # New field to store total ordered quantity
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('cancel', 'Cancel'),
        ('pending', 'Pending'),
        ('delivery', 'Delivery'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if not i.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

    def set_order_delivered(self):
        if self.status == 'delivery':
            orderitems = self.orderitem_set.all()
            for item in orderitems:
                item.product.total -= item.quantity
                item.product.save()

class OrderItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=2, null=False)
    zipcode = models.CharField(max_length=5,null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address