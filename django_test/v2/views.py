from django.shortcuts import render

def index(request):
    return render(request, 'v2/index.html')