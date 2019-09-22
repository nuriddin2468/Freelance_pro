from django.shortcuts import render
from django.views import generic
from company import models
from django.shortcuts import redirect
# Create your views here.


class CompanyListView(generic.ListView):
    template_name = 'company/company_list.html'
    model = models.CompanyModel
    paginate_by = 10


class CompanyDetailView(generic.DetailView):
    template_name = 'company/company_detail.html'
    model = models.CompanyModel
