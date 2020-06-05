from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    d={'addme':'Help Page'}
    return render(request,'help/index.html',context=d)