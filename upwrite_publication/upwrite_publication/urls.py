from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from news.admin import custom_admin_site


urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('', include('news.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




