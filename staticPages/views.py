from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
# Create your views here.


def indexs(request):
    return render(request, 'staticPages/index.html', {
    })

