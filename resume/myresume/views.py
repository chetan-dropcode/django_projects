from django.shortcuts import render

# Create your views here.


def portfolio(request):
    return render(request,'myinfo/base.html')

def idea(request):
    return render(request,'ideamagix/index.html')

def watch(request):
    return render(request,'watch/index.html')