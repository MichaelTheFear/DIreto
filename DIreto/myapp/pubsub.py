from DIreto.types import Response, Error
from models import Usuario, Postagem, Categoria
from emails import send_email

publisher_args = ['titulo','conteudo','categoria','usuario']

def publisher(post:dict) -> Response:
    for arg in publisher_args:
        if post.get(arg) is None:
            return (None,f"{arg} não foi definido passado")
    
    
    post_creator = Usuario.objects.get(email=post.get('usuario'))
    
    post_cat = Categoria.objects.get(nome=post.get('categoria'))

    new_post = Postagem(titulo=post.get('titulo'),
                    conteudo=post.get('conteudo'),
                    usuario=post_creator,
                    categoria=post_cat
                    ) 
    
    new_post.save()
    title:str = post.get('titulo')  # type: ignore
    content:str = post.get('conteudo') # type: ignore
    send_email(content,title)

    data = new_post.id

    return (data,None)

def subscriber(cat:str, user_email:str) -> Response:
    try:
        user = Usuario.objects.get(email=user_email)
        categoria = Categoria.objects.get(nome=cat)
        user.categoria.add(categoria)
        user.save()
        return (user.__dict__,None)
    except:
        return (None,"Usuario ou categoria não existem")
    



