from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def redirect_to_AdminPage(request):
    return redirect('Login')

def Login_view(request):
    if(request.user.is_authenticated):
        return(HttpResponse('loged in'))
    else:
        if(request.method == 'POST'):
            print(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username , password = password)
            if( user is not None):
                login(request,user)
                print(user)
                return redirect('ControlPanel')
            
        if(request.method == 'GET'):
            return render(request,'AdminPage/login.html')


def ControlPanel(request):
    pass