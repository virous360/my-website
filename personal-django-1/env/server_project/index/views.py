from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
def home(request: HttpRequest):
    if request.COOKIES == {}:
        return sign_in(request)
    else :
        return render(request, "index.html")
def sign_in(request: HttpRequest):
    return render(request,"sign_in.html")