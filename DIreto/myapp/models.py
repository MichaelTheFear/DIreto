from django.db import models
import uuid
# Create your models here.
#Usuario
class Categoria(models.Model):
    nome = models.CharField(primary_key=True,max_length=100)

    def __str__(self):
        return self.nome




class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    senha = models.CharField(max_length=50)
    matricula = models.CharField(max_length=7)
    informante = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    notificacao_por_email = models.BooleanField(default=True)
    notificacao_por_push = models.BooleanField(default=True)
    categoria = models.ManyToManyField(Categoria)


    def __str__(self):
        return self.nome


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