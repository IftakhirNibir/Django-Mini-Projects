from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   path('admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
    path("", include("Core.urls")),
    path("Item/", include("Jewelry.urls")),
    path("dashboard/", include("Dashboard.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
