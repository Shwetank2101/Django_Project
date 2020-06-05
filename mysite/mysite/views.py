from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at site/views.py index.")
def hello(request):
    return HttpResponse("Hello welcome to home page")
def time(request):
    now = datetime.datetime.now()
    t = "Time is {}".format(now)
    return HttpResponse(t)
