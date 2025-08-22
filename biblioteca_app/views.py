from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Emprestimo

def home(request):
    return render(request, 'home.html') 

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca_app/livros/lista.html', {'livros': livros})

def form_livro(request, id=None):
    if id:
        livro = get_object_or_404(Livro, id=id)
    else:
        livro = None

    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        genero = request.POST['genero']
        quantidade = int(request.POST['quantidade'])
        if livro:
            livro.titulo = titulo
            livro.autor = autor
            livro.genero = genero
            livro.quantidade = quantidade
            livro.save()
        else:
            Livro.objects.create(titulo=titulo, autor=autor, genero=genero, quantidade=quantidade)
        return redirect('lista_livros')

    return render(request, 'emprestimos/form.html', {'livro': livro})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('lista_livros')

def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos/lista.html', {'emprestimos': emprestimos})

def form_emprestimo(request):
    livros = Livro.objects.filter(quantidade__gt=0)
    if request.method == 'POST':
        livro_id = request.POST['livro']
        livro = get_object_or_404(Livro, id=livro_id)
        Emprestimo.objects.create(usuario='Usuario_Teste', livro=livro)
        livro.quantidade -= 1
        livro.save()
        return redirect('lista_emprestimos')
    return render(request, 'emprestimos/form.html', {'livros': livros})

def devolver_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if not emprestimo.devolvido:
        emprestimo.devolvido = True
        emprestimo.livro.quantidade += 1
        emprestimo.livro.save()
        emprestimo.save()
    return redirect('lista_emprestimos')
