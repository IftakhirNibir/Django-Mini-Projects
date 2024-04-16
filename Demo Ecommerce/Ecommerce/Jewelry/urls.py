from django.urls import path
from .views import *

app_name = 'Jewelry'

urlpatterns = [
    path('new/', new, name="new"),
    path('<int:pk>/edit', edit, name="edit"),
    path("<int:pk>/", detail, name="detail"),
    path('<int:pk>/delete', delete, name="delete"),
    path('all_items', items, name="items"),
    path('cart/', cart, name="cart"),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('cart/update_item/', updateItem, name="update_item"),
    path('update_item/', updateItem, name="update_item"),
    path('checkout/', checkout_page, name="checkout_page"),
    path('checkout/process_order/', processOrder, name="process_order"),
    path('cart/clear_cart/', clear_cart, name='clear_cart'),
]

