from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from Jewelry.views import updateItem

from .forms import LoginForm
app_name = "Core"


urlpatterns = [
    path("", views.index, name="index"),
    path("Signup/", views.signup, name="signup"),
    path("Login/", views.login, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('update_item/', updateItem, name="update_item"),
    path('blogs/', views.blog_detail, name='blog_detail'),
]