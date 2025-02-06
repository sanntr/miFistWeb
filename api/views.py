from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .api_service import inData
# Create your views here.

def reponsAticles(request):
    return render(request,'articles.html',  {'result':inData()} )

