from django.urls import path
from .views import FanPediaDetailView, FanPediaCreateView

urlpatterns = [
    path('create/', FanPediaCreateView.as_view(), name='fanpedia_create'),
    path('<slug:slug>/', FanPediaDetailView.as_view(), name='fanpedia_detail'),
]