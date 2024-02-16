from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request): 
    
    peoples = [
        {"name" : "Sajib", "age": "28"},
        {"name" : "Sajid", "age": "23"},
    ]
    

    return render(request, "index.html", context = {"peoples": peoples, 'page' : "Home" })

def contact(request): 
    context = {'page' : "Contact"}
    return render(request, "contact.html", context)

def success_page(request):
       return HttpResponse("""<h1>This is Sucess Page...</h1>
                           <br>
                           <h1>Hello</h1>""")