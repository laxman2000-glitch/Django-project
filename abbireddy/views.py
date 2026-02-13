
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

def login_page(request):
    message = None

    if request.method == "POST":

        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message = "Invalid username or password"
    return render(request,'login.html',{'message':message})
def logout_page(request):
    logout(request)
    return redirect('login_user')

def user_update(request):
    message = "None"
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = request.user

        if User.objects.exclude(id=user.id).filter(username=username).exists():
            return render(request,'update.html',{'message':'username already exists'})
        user.username = username
        if password:
            user.set_password(
                
                password)
        user.save()

        message = "username and password updated"
        return redirect('login_user')
        
    return render(request, 'update.html',{'message': message})


@login_required(login_url='login_user')
def laxman_page(request):
    return render(request,'index.html')
@login_required(login_url='login_user')
def contactus(request):
    return render(request,'contact.html')
