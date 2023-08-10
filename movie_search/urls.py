from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('https://watchnext.up.railway.app', include('watch_next.urls')),
]
