from django.shortcuts import render
from django.views import generic
from company.models import CompanyModel
from django.shortcuts import redirect
from jobs.models import JobsFLModel
from django.shortcuts import get_object_or_404
# Create your views here.


class CompanyListView(generic.ListView):
    template_name = 'company/company_list.html'
    model = CompanyModel
    paginate_by = 10


class CompanySearchView(generic.ListView):
    template_name = 'company/company_list.html'
    paginate_by = 10

    def get_queryset(self):
        return CompanyModel.objects.filter(name__icontains=self.request.GET['q'])

    def get_context_data(self, *args, **kwargs):
        context = super(CompanySearchView, self).get_context_data(*args, **kwargs)
        if self.request.method == 'GET' and self.request.GET['q']:
            context['search'] = True
        return context


class CompanyDetailView(generic.DetailView):
    template_name = 'company/company_detail.html'
    model = CompanyModel

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        comp = get_object_or_404(CompanyModel, id=self.kwargs['pk'])
        obj = JobsFLModel.objects.filter(job_given=comp.user)
        if not obj:
            context['jobs'] = False
        else:
            context['jobs'] = obj
        return context
