from django.urls import path, include
from company import views


urlpatterns = [
    path('list/', views.CompanyListView.as_view(), name="company-list"),
    path('detail/<str:pk>', views.CompanyDetailView.as_view(), name="company-detail"),
    path('search/', views.CompanySearchView.as_view(), name="company-search"),
]
