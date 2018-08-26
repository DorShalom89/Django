from django.urls import path
from Cars import views

urlpatterns = [
    path('car/', views.car),
    path('owner/', views.owner),
    path('', views.index)
]