from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('http://web-production-8a28.up.railway.app/', include('watch_next.urls')),
]
