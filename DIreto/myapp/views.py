from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Usuario as User
from myapp.auth import validate_login, signin
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        res, error = validate_login(request)
        if res:
            return HttpResponse("O usuário autenticado com sucesso!")
        else:
            return HttpResponse(error)
        


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        res, error = signin(request)
        if res:
            return HttpResponse("O usuário foi cadastrado com sucesso!")
            # Talvez mandar ele para a proxima pagina? 
        else:
            return HttpResponse(error)

def index(request):
    return HttpResponse("Home page")

def search(request):
    return HttpResponse("Busca")

def login_error(request):
    return HttpResponse("Login inválido")

def cadastro_error(request):
    return HttpResponse("Cadastro inválido")

def esqueci_senha(request):
    return HttpResponse("Esqueci minha senha")

@login_required(login_url='/login/')
def logout(request):
    return HttpResponse("Logout")

@login_required(login_url='/login/')
def timeline(request):
    return HttpResponse("Logado")

@login_required(login_url='/login/')
def configuracoes(request):
    return HttpResponse("Configurações")

@login_required(login_url='/login/') # fazer com que seja necessario ser staff 
def novo_post(request):
    return HttpResponse("Novo post")

def novo_post_error(request):
    return HttpResponse("Erro ao criar post")