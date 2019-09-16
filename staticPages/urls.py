from django.urls import path, include
from staticPages import views

urlpatterns = [
    path('dashboard/', views.indexs)
]