from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    my_dict={'insert_me':'Hello, world! You are at the polls index.'}
    return render(request,"polls/index.html",context=my_dict)
def pic(request):
    d={'pik':'We are friends'}
    return render(request,"polls/pic.html",context=d)
