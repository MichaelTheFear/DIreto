from myapp.types import Response, Error
from myapp.models import Usuario as User
from django.contrib.auth import authenticate, login as django_login

def validate_login(request) -> Response:

    if request.POST.get('username') is None:
        return (None,"Usuário não foi definido passado")
    if request.POST.get('password') is None:
        return (None,"Senha não foi definida passada")

    email = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, email = email, password = password)
    if user is not None:
        django_login(request,user)
        return (True,None)
    
    return (None,"Usuário ou senha inválidos!")


required_fields = ['email','first_name','last_name','password','confirm_password','matricula']

def signin(request) -> Response:
    POST = request.POST
    user_att = {}
    for field in required_fields:
        post_field = POST.get(field)
        if post_field in [None,''," "]:
            return (None,f"{field} não foi definido passado")
        else:
            user_att[field] = post_field
    
    if user_att['password'] != user_att['confirm_password']:
        return (None,"Senhas não conhecidem!")

    user_att.pop('confirm_password')
    user = User.objects.filter(email=user_att['email']).first()
    if user is not None:
        return (None,f"Usuário {user_att['email']} já existe!")

    user = User.objects.create_user(**user_att) # type: ignore
    user.save()

    return (True,None)
    

