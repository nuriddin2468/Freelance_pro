from django.shortcuts import render
from django.views import generic
from accounts.models import EmployerModel
from django.shortcuts import redirect
from jobs.models import JobsModel
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout, login
# Create your views here.


class CompanyListView(generic.ListView):
    template_name = 'accounts/employers_list.html'
    model = EmployerModel
    paginate_by = 10


class CompanySearchView(generic.ListView):
    template_name = 'accounts/employers_list.html'
    paginate_by = 10

    def get_queryset(self):
        return EmployerModel.objects.filter(name__icontains=self.request.GET['q'])

    def get_context_data(self, *args, **kwargs):
        context = super(CompanySearchView, self).get_context_data(*args, **kwargs)
        if self.request.method == 'GET' and self.request.GET['q']:
            context['search'] = True
        return context


class CompanyDetailView(generic.DetailView):
    template_name = 'accounts/employer_detail.html'
    model = EmployerModel

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        comp = get_object_or_404(EmployerModel, id=self.kwargs['pk'])
        obj = JobsModel.objects.filter(job_given=comp.user)
        if not obj:
            context['jobs'] = False
        else:
            context['jobs'] = obj
        return context


class LogoutRedirectView(generic.RedirectView):
    pattern_name = 'dashboard'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)


class LoginRedirectView(generic.RedirectView):
    pattern_name = 'dashboard'

    def post(self, request, *args, **kwargs):
        print(request.POST['username'])
        login(request, request.POST['username'], request.POST['password'])
