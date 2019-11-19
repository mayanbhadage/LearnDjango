from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    str = "<h1> My Second App </h1>"
    return HttpResponse(str)

def help(request):
    my_dict = {'here': "Help page form views.py"}
    return render(request,'AppTwo/help.html',context=my_dict)
