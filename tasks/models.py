from django.db import models
from django.forms import ModelForm

# Create your models here.
class Task(models.Model):
    STATUS = (('1', 'Doing'), ('2', 'Done'))
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    done = models.CharField(max_length=1, choices=STATUS)
    data_criacao = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        db_table = 'tarefa'


class TarefaForm(ModelForm):
    class Meta:
        model = Task
        fields = ('titulo', 'descricao')
