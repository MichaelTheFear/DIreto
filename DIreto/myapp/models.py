from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import uuid
# Create your models here.
#Usuario
class Categoria(models.Model):
    nome = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, db_index=True,primary_key=True)
    matricula = models.CharField(max_length=7)
    informante = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    notificacao_por_email = models.BooleanField(default=True)
    notificacao_por_push = models.BooleanField(default=True)
    categoria = models.ManyToManyField(Categoria)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email


class Postagem(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    data_do_evento = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo