from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def notice(request):
    Notices = Notice.objects.all()
    return render(request, 'notice.html',{'Notices':Notices})