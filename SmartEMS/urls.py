from django.contrib import admin
from django.urls import path, include
from customUserAuth.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('customUserAuth.urls')),
]
