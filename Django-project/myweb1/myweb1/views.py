from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("<h1>Welcome to the about page</h1>")

def info(request):
    return HttpResponse("<h3>Welcome to the info page</h3>")

def default_page(request):
    return HttpResponse("<h3>Welcome to the first default page</h3>")

def posts(request, sid):  # Assuming you only want one 'posts' function
    return HttpResponse(sid)

def myhome(request):
    return render(request, "myhome.html")

def index(request):
    return render(request, "index.html")

def test(request):  # Corrected the 'requests' typo
    return HttpResponse("<h1>I am just testing the usability to this development platform.</h1>")

def djangohome(request):
    return render(request, "djangohome.html")

def homepass(request):
    data = {  # Using a dictionary for clarity and readability
        'title': 'mypage',
        'fdata': 'Welcome to Homepage',
        'age': [10, 20, 30, 40, 50],
        'lanlist': ['python', 'java', 'c', 'c++', 'c#'],
        'student_info': [
            {'name': 'ram', 'age': 20, 'address': 'ktm'},
            {'name': 'shyam', 'age': 22, 'address': 'bkt'},
        ]
    }
    return render(request, "hpass.html", data)
def mygetform(request):
    res = None  # Initialize res to None or some default value
    try:
        if request.method == "GET":
            n1 = int(request.GET.get("num1", 0))  # Default to 0 if not found
            n2 = int(request.GET.get("num2", 0))  # Default to 0 if not found
            res = n1 + n2
    except Exception as e:
        print(e)  # Log or handle the exception as needed
    return render(request, "mygetform.html", {"result": res})
def mypostform(request):
    res = 0  # Initialize res to None or some default value
    data={}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            res = n1 + n2
            data={
                'res':res,
                'n1':n1,
                'n2':n2,
            }
    except :
        pass
    return render(request, "mypostform.html", data)