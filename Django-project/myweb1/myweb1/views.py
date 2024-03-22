from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return HttpResponse("<h1> Welcome to the about pages ")
def info(request):
    return HttpResponse("<h3> Welcome to the infos page ")

def default_page(request):
    return HttpResponse("<h3> Welcome to the first default page ")
def posts(request,sid):
   return HttpResponse(sid)
def posts(request,sid):
    return HttpResponse(sid)
def myhome(request):
    return render(request,"myhome.html")

def index(request):
    return render(request,"index.html")

def test(requests):
    return HttpResponse("<h1> I am just testing the usability to this development platform. ")

def djangohome(request):
    return render(request, "djangohome.html")