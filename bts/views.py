from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'bts/index.html')

def new_release(request):
    return HttpResponse('new release')
