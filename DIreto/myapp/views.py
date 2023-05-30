from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Usuario as User
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login_auth(request,user)

            return HttpResponse(f"Usuário {email} autenticado com sucesso!")
        else:
            return HttpResponse("Usuário ou senha inválidos!")
        


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if email is None:
            return HttpResponse("Email não pode ser nulo!")

        print(email)
        user = User.objects.filter(email=email).first()
        if user is not None:
            return HttpResponse(f"Usuário {username} já existe!")
        
        user = User.objects.create_user(username, email, password, informante=True, notificacao_por_email=True, notificacao_por_push=True, matricula="1234567") # type: ignore
        user.save()

        return HttpResponse(f"Cadastro realizado com sucesso {username}!")

def index(request):
    return HttpResponse("Home page")

@login_required(login_url='/login/')
def timeline(request):
    return HttpResponse("Logado")
