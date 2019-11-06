from django.shortcuts import render
from django.views import generic
from django.views import View
from jobs.models import JobsModel, ProposalModel
from accounts.models import EmployerModel
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from jobs.forms import ProposalForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


class JobsListView(generic.ListView):
    template_name = 'jobs/jobs_list.html'
    model = JobsModel


class JobsDetailView(generic.DetailView):
    template_name = 'jobs/jobs_detail.html'
    model = JobsModel

    def get_context_data(self, **kwargs):
        context = super(JobsDetailView, self).get_context_data(**kwargs)
        obj = get_object_or_404(JobsModel, pk=self.kwargs['pk'])
        obj = EmployerModel.objects.get(user=obj.job_given.user)
        context['company'] = obj
        return context


class ProposalDetailView(generic.DetailView):
    template_name = 'jobs/proposal_detail.html'
    model = ProposalModel


class ProposalAddView(generic.View):
    template_name = 'jobs/proposal_add.html'

    def get(self, request, *args, **kwargs):
        job = get_object_or_404(JobsModel, pk=self.kwargs['pk'])
        form = ProposalForm()
        return render(request, self.template_name, {
            'job': job,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        job = get_object_or_404(JobsModel, pk=self.kwargs['pk'])
        form = ProposalForm(request.POST)
        form.user = request.user.id
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            job.proposals.add(data)
            job.save()
            return redirect('jobs-detail', job.id)
        else:
            form = ProposalForm()
            return render(request, self.template_name, {
                'job': job,
                'form': form,
            })



