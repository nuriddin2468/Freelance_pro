from django.urls import path, include
from accounts import views


urlpatterns = [
    path('employers/list/', views.CompanyListView.as_view(), name="employers-list"),
    path('employer/detail/<str:pk>', views.CompanyDetailView.as_view(), name="employer-detail"),
    path('employers/search/', views.CompanySearchView.as_view(), name="employers-search"),
    path('logout/', views.LogoutRedirectView.as_view(), name='logout'),
    path('login/', views.LoginRedirectView.as_view(), name='login'),
]
