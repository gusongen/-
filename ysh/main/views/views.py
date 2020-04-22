from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return JsonResponse({'mag': 'hello'})


def login(request):
    if request.method == 'GET':
        return render(request, 'dengru.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'zhuce.html')


def main(request):
    if request.method == 'GET':
        return render(request, 'zhuye.html')


def classify(request):
    if request.method == 'GET':
        return render(request, 'fenlei.html')
