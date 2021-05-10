from django.shortcuts import render
from .models import Provider
# Create your views here.
def info(request):
    return render(request, 'alert.html')

