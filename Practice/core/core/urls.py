from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name="receipes"),
    path('delete_receipe/<id>/',delete_receipe, name="delete"),
    path('update_receipe/<id>/',update_receipe, name="update"),
    path('register/', user_register, name="user_register"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




