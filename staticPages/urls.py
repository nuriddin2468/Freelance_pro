from django.urls import path, include
from staticPages import views


urlpatterns = [
    path('dashboard/', views.indexs, name="dashboard"),
    path('howitworks/', views.howitworks, name='howitworks')
]
