from django.contrib import admin
from .models import SavedItem
from Jewelry.models import Order, OrderItem, ShippingAddress
# Register your models here.

admin.site.register(SavedItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'get_ordered_quantity', 'get_total_amount', 'date_ordered', 'transaction_id', 'status')
    inlines = [OrderItemInline]  

    def get_ordered_quantity(self, obj):
        return ", ".join(str(item.quantity) for item in obj.orderitem_set.all())

    get_ordered_quantity.short_description = 'Ordered Quantity'

    def get_total_amount(self, obj):
        return obj.get_cart_total

    get_total_amount.short_description = 'Total Amount'

admin.site.register(Order, OrderAdmin)