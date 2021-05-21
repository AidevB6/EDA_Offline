from django.shortcuts import render

# Create your views here.


def eda_views(request):
    return render(request,'eda.html',{})
