from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Jewelry.models import Item, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import SavedItem
from Jewelry.models import OrderItem, Order, ShippingAddress, Item
from django.db.models import Sum

# Create your views here.
@login_required
def dashboard(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    sold_items_count = items.filter(is_sold=True).count()
    unsold_items_count = items.filter(is_sold=False).count()

    context = {
        'items': items,
        'categories': categories,
        'sold_items_count': sold_items_count,
        'unsold_items_count': unsold_items_count,
    }

    return render(request, 'dashboard.html', context)

@login_required
def profile(request):
    saveditems = SavedItem.objects.filter(user=request.user)
    
    # Retrieve all completed orders for the user
    user_orders = Order.objects.filter(customer=request.user, complete=True)
    
    # Retrieve order items for all completed orders
    user_order_items = OrderItem.objects.filter(order__in=user_orders)
    
    context = {'saveditems': saveditems, 'user_order_items': user_order_items}
    return render(request, 'profile.html', context)



@login_required
def save_item(request, item_id):
    user = request.user
    item = get_object_or_404(Item, pk=item_id)
    
    # Check if the item is already saved by the user
    saved_item = SavedItem.objects.filter(user=user, item=item).first()

    if saved_item:
        # If already saved, remove it
        saved_item.delete()
    else:
        # If not saved, save it
        SavedItem.objects.create(user=user, item=item)

    return redirect('Dashboard:profile')


def order_detail(request):
    orders = Order.objects.filter(complete=True)
    
    order_items = []
    
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_items.extend(items)
    
    context = {
        'orders':orders,
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'order_details.html', context)

def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_item = OrderItem.objects.filter(order=order)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('Dashboard:order_detail')
    
    return render(request, 'edit_order.html', {'order': order,'order_item':order_item})


def inventory(request):
    items = Item.objects.all()
    
    for item in items:
        total_ordered_quantity = OrderItem.objects.filter(product=item).aggregate(total_ordered=Sum('quantity'))['total_ordered']
        if total_ordered_quantity:
            item.total_ordered_quantity = total_ordered_quantity
        else:
            item.total_ordered_quantity = 0
        
    context = {
        'items': items,
    }
    return render(request, 'inventory.html', context)



