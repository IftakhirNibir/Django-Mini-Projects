from django.urls import path 
from .views import *
from Jewelry.views import updateItem

app_name = 'Dashboard'

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path('profile/update_item/', updateItem, name="update_item"),
    path("profile/", profile, name="profile"),
    path('save_item/<int:item_id>/', save_item, name='save_item'),
    path('order_details/', order_detail, name='order_detail'),
    path('edit_order/<int:order_id>/', edit_order, name='edit_order'),
    path('inventory/', inventory, name='inventory'),
]