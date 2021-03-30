from django.shortcuts import render
from .models import *

# Create your views here.
def conime(request):
    return render(request, 'canime/Conime.html')