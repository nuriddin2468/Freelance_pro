from django.shortcuts import render

# Create your views here.


def indexs(request):
    return render(request, 'staticPages/index.html')