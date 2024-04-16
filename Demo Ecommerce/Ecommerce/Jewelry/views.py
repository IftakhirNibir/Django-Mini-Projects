from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from django.db.models import Q
from .forms import *
import json
import uuid
from .utils import cookieCart, cartData
import datetime
# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item,pk=pk)

    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]

    context = {
        'item': item,
        'related_items': related_items
    }
    
    return render(request,"detail.html",context)

def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.all()
    
    # Provide default values for category_id and main_category_id
    category_id = request.GET.get('category', 0)
    main_category_id = request.GET.get('main_category', 0)

    categories = Category.objects.all()
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()

    # Ensure category_id and main_category_id are not empty before filtering
    if main_category_id and main_category_id.isdigit():
        items = items.filter(main_category_id=main_category_id)

    if category_id and category_id.isdigit():
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query))

    return render(request, 'allitems.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'main_categories': main_categories,
        'main_category_id': int(main_category_id)
    })

@require_POST
def delete_item(request, item_id):
    # Get the cart item to delete
    cart_item = get_object_or_404(CartItem, id=item_id)

    # Implement logic to delete the cart item
    cart_item.delete()

    # Redirect to the cart page after deletion
    return redirect('Jewelry:cart') 


@login_required 
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)#create object but not save in the database
            item.created_by = request.user
            item.save()

            return redirect('Jewelry:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'form.html', {
        'form': form,
        'title': 'Create New Jewelry',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('Dashboard:dashboard')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
   
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('Jewelry:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'form.html', {
        'form': form,
        'title': 'Edit Jewelry Info',
    })

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user
    product = Item.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


@login_required
def checkout_page(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    last_order = Order.objects.filter(customer=request.user, complete=True).last()
    
    shipping_address = None
    if last_order:
        shipping_address = ShippingAddress.objects.filter(customer=request.user, order=last_order).first()
    
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'shipping_address': shipping_address}
    return render(request, 'checkout.html', context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
            order.status = 'pending'
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print("User is not logged in...")

    return JsonResponse('Payment complete..', safe=False)


def clear_cart(request):
    if request.method == 'POST':

        # order = Order.objects.filter(complete=False, customer=request.user)

        OrderItem.objects.filter(order__customer=request.user, order__complete=False).delete()

        return JsonResponse({'message': 'Cart cleared successfully'}, status=200)
    else:

        return JsonResponse({'error': 'Invalid request method'}, status=400)

