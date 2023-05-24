from typing import Optional
from models import Usuario, Postagem, Categoria


publisher_args = ['titulo','conteudo','categoria','usuario']
Data = Optional[str]

def send_email(content:str,cat:Union[Categoria,list[Categoria]]) -> None:
    pass


def publisher(post:dict) -> tuple(Data,Data):
    for arg in publisher_args:
        if post.get(args) is None:
            return (None,f"{args} não foi definido passado")
    
    
    # post_creator = Usuario.pegar usuario
    # post_cat = Postagem.pega categoria

    new_post = Post(titulo=post.get('titulo'),
                    conteudo=post.get('conteudo'),
                    usuario=post_creator,
                    categoria=post_cat
                    ) 
    
    new_post.save()
    send_emails(post.get('titulo'),post_cat)
    

    return (data,error)