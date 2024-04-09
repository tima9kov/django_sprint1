from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def about(request):
    return HttpResponse('fuck')

def rules(request):
    return HttpResponse('fuck')