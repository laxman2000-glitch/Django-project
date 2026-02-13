from django.shortcuts import render, redirect
from .models import Details,Shiva
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def register_page(request):
    message = None

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        fathername = request.POST.get('fathername')
        mobilenumber = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            message = "Passwords do not match"
        elif User.objects.filter(username=username).exists():
            message = "Username already exists"
        else:
            Shiva.objects.create(
                firstname= firstname,
                lastname= lastname,
                fathername= fathername,
                email= email,
                mobilenumber= mobilenumber
                )
            user = User.objects.create_user(
                username=username,
                password=password
            )
            login(request, user)
            return redirect('login_user')

    return render(request, 'register.html', {'message': message})


def contact_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Details.objects.create(
            name = name, 
            email=email, 
            subject=subject, 
            message=message
            )
        return redirect('contact_page')
    abbireddy = Details.objects.order_by()
    return render(request, 'contact.html',{'abbireddy':abbireddy})

def search_page(request):
    message = None
    if request.method == "POST":
        email= request.POST.get('email')
        message= Details.objects.filter(email=email)

    return render(request,'contact.html',{'message':message})

def user_details(request):
    message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        
        message = Shiva.objects.filter(email=email)

    return render(request,'userdetails.html',{'message': message})
         
