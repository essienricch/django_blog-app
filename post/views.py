from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, 'hello.html')


def login(request):
    return render(request, 'login.html')


def greet(request):
    return HttpResponse('Trust you are good')


def locked(request):
    return HttpResponse("Life is Good, Enjoy the Moment whilst you still can")
