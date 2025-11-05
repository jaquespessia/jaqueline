from django.shortcuts import render, redirect, get_object_or_404

from projetos.models import Projeto
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
    projetos = Projeto.objects.all ()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get ('projeto') #pega o id do projeto selecionado
        projeto_selecionado = Projeto.objects.get (pk=projeto_id)
        Tarefa.objects.create (titulo=titulo, descricao=descricao, projeto=projeto_selecionado)
        Tarefa.objects.create(titulo = titulo, descricao = descricao)   
        return redirect('lista_tarefas')
    return render (request, 'tarefas/form_tarefa.html', {'projetos': projetos})

#métodos HTTP
#POST: envia dados para o servidor
#GET: buscar dados no servidor
#PUT: atualizar recursos existetes
#DELETE: remove recursos selecionados

def alterar_tarefa(request, tarefa_id):
    projetos = Projeto.objects.all ()
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get ('projeto') 
        concluida = request.POST.get('concluida') == 'on' 

        projeto_selecionado = get_object_or_404 (Projeto , pk=projeto_id)

      
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluida = concluida
        tarefa.projeto = projeto_selecionado
        tarefa.save()
        
        return redirect('lista_tarefas')

    context = {
        'tarefa': tarefa,
        'projetos': projetos,
    }
    return render(request, 'tarefas/form_tarefa.html', context)

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa})