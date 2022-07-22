from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template=loader.get_template("interface/index.html")
    context={}
    return HttpResponse(template.render(context,request))

#inteface de l'utilisateur
def connexion(request):
    return render(request,'acceuil/interface.html')