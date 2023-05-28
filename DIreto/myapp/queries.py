from DIreto.types import Response, Error
from models import Usuario

def create_user(email:str, password:str, name:str) -> Response:
    try:
        user = Usuario(email=email,password=password,nome=name)
        user.save()
        response = {x:y for x,y in user.__dict__.items() if x not in ['_state', 'password']}

        return (response,None)
    except:
        return (None,"Email já cadastrado")
    

