from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['User_Name']
        firstname = request.POST['First_Name']
        lastname = request.POST['Last_Name']
        email = request.POST['Email']
        password = request.POST['Password']
        confirmpw = request.POST['Password1']
        if password == confirmpw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User Name already taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('register')
            elif User.objects.filter(password=password).exists():
                messages.info(request,"Password already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)

                user.save();
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
            return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('login')
