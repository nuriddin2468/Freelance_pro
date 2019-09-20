from django.urls import path, include
from staticPages import views


urlpatterns = [
    path('dashboard/', views.indexs, name="dashboard"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('registration/', views.RegisterView.as_view(), name='register')
]