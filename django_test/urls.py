from django import views
from django.contrib import admin

admin.autodiscover()
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),
    path('testapp/', include('testapp.urls')),
]
