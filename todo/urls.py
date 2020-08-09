from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/', views.completed, name='completed'),
    path('deleteAllCompleted/', views.deleteAllCompleted, name='deleteAllCompleted'),
]
