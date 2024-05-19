from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 


# Create your views here.

@login_required(login_url='/login/')
def receipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('receipe_name')
        description = data.get('receipe_description')
        image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name = name,
            receipe_description = description,
            receipe_image = image
        )

        return redirect('/receipes/')

    a = Receipe.objects.all()

    search = request.GET.get('search')

    if search:
        a = a.filter(receipe_name__icontains = search)

    context = {'datas':a}
    return render(request,'receipes.html',context) 


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('receipe_name')
        description = data.get('receipe_description')
        image = request.FILES.get('receipe_image')

        queryset.receipe_name = name 
        queryset.receipe_description = description 
        queryset.receipe_image = image 

        queryset.save()
        return redirect('/receipes/')

    context = {'data':queryset}
    
    return render(request,'receipe_update.html',context) 

def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_password = request.POST.get('check_password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already taken. Please try another')
            return redirect('/register/')

        if password != check_password:
            messages.error(request, "Passwords do not match.")
            return redirect('/register/')  

        try:
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)  # Hash the password
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('/register/')  
        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return redirect('/register/')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/receipes/')
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid Username')
            else:
                messages.error(request, 'Invalid Password')
            return redirect('/login/') 

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')



    