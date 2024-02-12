from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *

# Create your views here.

@login_required(login_url = "/login")
def receipes(request):
    if(request.method == "POST"):
            data = request.POST
            receipe_name = data.get('receipe_name')
            receipe_description = data.get('receipe_description')
            receipe_image = request.FILES.get('receipe_image')
    # print(receipe_name, receipe_description, receipe_image)
    
            Receipe.objects.create(
                receipe_name=receipe_name, 
                receipe_description=receipe_description, 
                receipe_image=receipe_image)

            return redirect("/receipes")
        
    queryset = Receipe.objects.all()
    
    if request.GET.get("search"):
        print(request.GET.get("search"))
        queryset = queryset.filter(receipe_name__icontains = request.GET.get("search")) |  queryset.filter(receipe_description__icontains = request.GET.get("search"))
        print(queryset)
    
    context = {"receipes": queryset, "search": request.GET.get("search")}
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
        queryset = Receipe.objects.get(id = id)
        queryset.delete()
        return redirect("/receipes")
    
def update_receipe(request, id):
        queryset = Receipe.objects.get(id = id)
        
        if(request.method == "POST"):
            data = request.POST
            receipe_name = data.get('receipe_name')
            receipe_description = data.get('receipe_description')
            receipe_image = request.FILES.get('receipe_image')
            
            queryset.receipe_name  = receipe_name
            queryset.receipe_description = receipe_description
            if receipe_image:
                queryset.receipe_image = receipe_image
                
            queryset.save()
            return redirect("/receipes")
           
            
        context={"receipe": queryset}
        return render(request, 'update_receipes.html', context)
    

def login_page(request):
    
     if(request.method == "POST"):
            data = request.POST
        
            username = data.get('username')
            password = data.get('password')
            
      
            print(User.objects.filter(username = username))
            
            if not User.objects.filter(username = username).exists():
                messages.error(request, "Invalid Username")
                return redirect('/login')
            
            user = authenticate(username= username, password = password)
            
            if user is None:
                 messages.error(request, "Invalid Password")
                 return redirect('/login')
            else:
                login(request, user)
                return redirect('/receipes/')

     return render(request, 'login.html')
    
def register_page(request):
    
    if(request.method == "POST"):
            data = request.POST
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            username = data.get('username')
            password = data.get('password')
            
            user = User.objects.filter(username = username)
            
            if(user.exists()):
                messages.error(request, "Userrname already taken.")
                return redirect('/register')
            
            user = User.objects.create(
                  first_name=first_name, 
                  last_name=last_name, 
                  username=username)
            
            user.set_password(password)
            user.save()
            
            messages.success(request, "Account Created Successfully.")
            
            return redirect("/register")
        
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')