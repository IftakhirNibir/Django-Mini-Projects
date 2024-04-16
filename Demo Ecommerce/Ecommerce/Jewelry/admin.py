from django.contrib import admin
from .models import Category, Item, MainCategory, SubCategory, Order, OrderItem, ShippingAddress
# Register your models here.

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Item)
# admin.site.register([Order,OrderItem,ShippingAddress])
