from django.shortcuts import render, redirect
from .models import Task, TarefaForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {'tarefas': Task.objects.all().order_by('-data_criacao')})

def list(request, pk):
    # get_object_or_404(Task, pk) ou Task.objects.get(pk=pk)
    return render(
        request, 'list.html', {'tarefa': Task.objects.get(pk=pk)}
    )

def create(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)            
            tarefa.done = '1'
            tarefa.save()
            return redirect('home')            
    else:
        return render(request, 'form.html', {'form': TarefaForm()})

def edit(request, pk):
    tarefa = Task.objects.get(pk=pk)
    form = TarefaForm(instance=tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa.save()
            return redirect('home')
    return render(request, 'edit.html', {'tarefa': tarefa, 'form': form})
