from django.urls import path, include
from company import views


urlpatterns = [
    path('list/', views.CompanyListView.as_view(), name="company-list"),
    path('detail/<int:pk>', views.CompanyDetailView.as_view(), name="company-detail"),
]
