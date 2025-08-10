from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from customUserAuth.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('customUserAuth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
