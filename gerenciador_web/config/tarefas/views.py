from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

def listar_tarefas(request):
    # 1. a busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()

    # 2. criamos um "dicionario do contexto" para enviar os dados ao template.
    # A chave 'minhas_tarefas' será a variável que usaremos no html.
    contexto = {
        'minhas_tarefas': tarefas_salvas 
    }

    # 3. renderizamos o tamplate, passando a requisição e o contexto com os dados.
    return render(request, 'tarefas/lista.html', contexto)

def detalhe_tarefa(request, tarefa_id):
    #Busca uma tarefa pelo id
    #Se não encontrar retorna um erro 404
    tarefa= get_object_or_404 (Tarefa, pk=tarefa_id)

    return render(request, 'tarefas/detalhe.html', {'tarefa':tarefa})

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo = titulo, descricao = descricao)   
        return redirect('listar_tarefas')
    return render (request, 'tarefas/form_tarefas.html')

#métodos HTTP
#POST: envia dados para o servidor
#GET: buscar dados no servidor
#PUT: atualizar recursos existetes
#DELETE: remove recursos selecionados

def alterar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        concluida = request.POST.get('concluida') == 'on' 

      
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluida = concluida
        
        tarefa.save()
        
        return redirect('lista_tarefas')

    context = {
        'tarefa': tarefa,
    }
    return render(request, 'tarefas/form_tarefas.html', context)

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefa')
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa})