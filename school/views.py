from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def notice(request):
    Notices = Notice.objects.all()
    return render(request, 'notice.html',{'Notices':Notices})

def free_board(request):
    Free_boards = Free_board.objects.all()
    return render(request, 'free.html',{'Free_boards':Free_boards})

def study_board(request):
    Study_boards = Study_board.objects.all()
    return render(request, 'study.html',{'Study_boards':Study_boards})

def contest_board(request):
    Contest_boards = Contest_board.objects.all()
    return render(request, 'contest.html',{'Contest_boards':Contest_boards})

def graduate_board(request):
    Graduate_boards = Graduate_board.objects.all()
    return render(request, 'graduate.html',{'Graduate_boards':Graduate_boards})

def club_board(request):
    Club_boards = Club_board.objects.all()
    return render(request, 'club.html',{'Club_boards':Club_boards})

def market_board(request):
    Market_boards = Market_board.objects.all()
    return render(request, 'club.html',{'Market_boards':Market_boards})