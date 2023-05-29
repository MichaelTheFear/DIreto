from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login_auth(request,user)

            return HttpResponse(f"Usuário {username} autenticado com sucesso!")
        else:
            return HttpResponse("Usuário ou senha inválidos!")
        


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username).first()
        if user is not None:
            return HttpResponse(f"Usuário {username} já existe!")
        
        user = User.objects.create_user(username, email, password)
        user.save()

        return HttpResponse(f"Cadastro realizado com sucesso {username}!")

def index(request):
    return HttpResponse("Home page")

@login_required(login_url='/login/')
def timeline(request):
    return HttpResponse("Logado")
