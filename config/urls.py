from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings
from config.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    # Rosetta i18n
    path('rosetta/', include('rosetta.urls')),
    path('order/', include('orders.urls')),
    # Pillow
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
