from django.shortcuts import render
from django.views import generic
from jobs.models import JobsFLModel
# Create your views here.


class JobsListView(generic.ListView):
    template_name = 'jobs/jobs_list.html'
    model = JobsFLModel