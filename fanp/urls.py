from django.contrib import admin
from django.urls import path, include
from fanpedia.views import FanPediaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', FanPediaView.as_view(), name='home'),  # Include FanPediaView for the home page
    path('fanpedia/', include('fanpedia.urls')),  # Include fanpedia URLs
]