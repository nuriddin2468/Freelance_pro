from django.urls import path, include
from jobs import views


urlpatterns = [
    path('list/', views.JobsListView.as_view(), name="jobs-list"),
]
