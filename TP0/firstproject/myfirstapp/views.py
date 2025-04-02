from django.shortcuts import render

# Create your views here

def formulaire(request):
    return render(request, 'myfirstapp/formulaire1/formulaire.html')

def traitement(request):
    nom=request.GET["nom"]
    email = request.GET["email"]
    sujet = request.GET["sujet"]
    message = request.GET["message"]
    return render(request, 'myfirstapp/formulaire1/traitement.html', {"nom": nom, "email": email, "sujet": sujet, "message": message})



def sphère(request):
    return render(request, 'myfirstapp/formulaire3/sphère.html')

