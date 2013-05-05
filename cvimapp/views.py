# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def list_cvs(request):
    return render_to_response('index.html')

def detail_cv(request):
    return None

def list_experiences(request):
    return render_to_response('experience.html')

def list_friends(request):
    return None

def detail_friend(request):
    return None

def login(request):
    return None
