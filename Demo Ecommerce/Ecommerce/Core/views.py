from django.shortcuts import render, redirect, get_object_or_404
from Jewelry.models import *
from Dashboard.models import SavedItem
from .forms import SignupForm
import json
from .models import Blog
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:4]
     # Ensure request.user is a concrete user instance
    user_instance = request.user if request.user.is_authenticated else None

    saved_item_id = SavedItem.objects.filter(user=user_instance).values_list('item__id', flat=True)
    
    context = {
        'items':items,
        'saved_item_id': saved_item_id,
    }
    return render(request,"index.html",context) 


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('Core:login')
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', {
        'form': form
    })

def login(request):
    return render(request, "login.html")


def blog_detail(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_details.html', {'blogs': blogs})