from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'SearchEngine/home.html')
def search(request):
    return render(request, 'SearchEngine/search.html')