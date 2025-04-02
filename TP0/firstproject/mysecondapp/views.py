from django.shortcuts import render

# Create your views here.

def fruit(request):
    return render(request, 'mysecondapp/formulaire2/fruit.html')