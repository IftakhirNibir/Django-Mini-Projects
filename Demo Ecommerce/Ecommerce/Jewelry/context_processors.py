from Dashboard.models import SavedItem 
from Core.models import Shop_Info, Blog, Slider , Notification
from .models import Order


def Saved_Items(request):
    user_instance = request.user if request.user.is_authenticated else None

    saved_item_id = SavedItem.objects.filter(user=user_instance).values_list('item__id', flat=True)

    return {'Saved_Item':saved_item_id}

def homepage_info(request):
    shopInfo = Shop_Info.objects.all()
    slider = Slider.objects.filter(status=True)
    blogs = Blog.objects.all()
    notification = Notification.objects.filter(display=True)

    return {'shopInfo': shopInfo, 'slider':slider, 'blogs':blogs , 'notification':notification}


def total_cart_items(request):
     user_instance = request.user if request.user.is_authenticated else None
     order, created = Order.objects.get_or_create(customer=user_instance, complete=False)
     cart_items = order.get_cart_items
     return {'cart_items':cart_items}


