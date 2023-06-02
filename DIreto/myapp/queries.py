from typing import Union
from DIreto.types import Response, Error
from models import Usuario, Postagem, Categoria

    
def _filter_posts_props(post:Postagem) -> dict:
    base_dict ={
        'id':post.id,
        'titulo':post.titulo,
        'conteudo':post.conteudo,
        'criado_em':post.criado_em,
        'categoria':[x.nome for x in Categoria.objects.filter(postagem=post)],
        'usuario':Usuario.objects.get(email=post.usuario.email).first_name,
    }

    if post.data_do_evento is not None:
        base_dict['data_do_evento'] = post.data_do_evento
    return base_dict
    

def _get_post_of_category(category_name: str) -> Response:
    cat = Categoria.objects.filter(nome=category_name).first()
    if cat is None:
        return (None,f"Categoria {category_name} não existe!")
    
    posts = Postagem.objects.filter(categoria=cat)
    if posts is None:
        return (None,f"Não há posts na categoria {category_name}!")

    filterd_posts = list(map(_filter_posts_props,posts))
    return (filterd_posts,None)

def get_posts_of_category(category_name: Union[str,list[str]]) -> Response:
    if category_name is None:
        return (None,"Categoria não foi definida ")
    if isinstance(category_name,str):
        return _get_post_of_category(category_name)
    else:
        posts = []
        for cat in category_name:
            post,error = _get_post_of_category(cat)
            if error is not None:
                return (None,error)
            posts.extend(post) # type: ignore

        return (posts,None)

def get_all_posts() -> Response:
    posts = Postagem.objects.all()

    if posts is None:
        return (None,"Não há posts!")
    
    filterd_posts = [_filter_posts_props(x) for x in posts]
    return (filterd_posts,None)


def get_post_by_title_or_content(title_or_content:str) -> Response:
    posts = Postagem.objects.filter(titulo__icontains=title_or_content) | Postagem.objects.filter(conteudo__icontains=title_or_content)
    if posts is None:
        return (None,f"Não há posts com o título ou conteúdo {title_or_content}!")
    
    filterd_posts = [_filter_posts_props(x) for x in posts]
    return (filterd_posts,None)

def get_all_categories() -> Response:
    categories = Categoria.objects.all()
    if categories is None:
        return (None,"Não há categorias!")
    
    
    return ([x.nome for x in categories],None)

def get_category(category_name:str) -> Response:
    cats = Categoria.objects.filter(nome=category_name)
    if cats is None:
        return (None,f"Categoria {category_name} não existe!")
    
    return ([x.nome for x in cats],None)


def search_by_keywords(keyword:str) -> Response:
    cats,cerror = get_category(keyword)
    posts,perror = get_post_by_title_or_content(keyword)
    return ([cats,posts], None if cerror is None and perror is None else f"{cerror} {perror}")
    





