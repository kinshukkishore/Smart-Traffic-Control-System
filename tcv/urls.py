from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('intersection/<int:intersection_id>/', views.intersection),
    path('traffic-lights/<int:intersection_id>/', views.traffic_lights),
    path('vehicles/<int:intersection_id>/', views.vehicles)
]
