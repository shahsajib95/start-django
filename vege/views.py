from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *

User = get_user_model()
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

from django.db.models import Q, Sum


def get_students(request):
 
    queryset = Student.objects.all()
    

    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) | 
            Q(department__department__icontains = search) |
            Q(student_email__icontains = search)|
            Q(student_id__student_id__icontains = search)
            )
     
     
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context={"students": page_obj, "page_obj": page_obj}
    return render(request, 'report/student.html', context)
  

from .seed import generate_report_card


def see_mark(request, student_id):
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)

    total_marks =  queryset.aggregate(total_marks = Sum('marks'))
    
    context={"student_mark": queryset, "total_marks" : total_marks}
    return render(request, 'report/see_mark.html', context)