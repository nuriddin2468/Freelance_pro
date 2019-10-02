from django.urls import path, include
from jobs import views


urlpatterns = [
    path('list/', views.JobsListView.as_view(), name="jobs-list"),
    path('detail/<str:pk>', views.JobsDetailView.as_view(), name="jobs-detail"),
    path('proposal/add/<str:pk>', views.ProposalAddView.as_view(), name="proposal-add"),
    path('proposal/detail/<str:pk>', views.ProposalDetailView.as_view(), name="proposal-detail"), # Доделать нужно!
]
