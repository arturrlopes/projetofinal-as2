from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Publicacao

def pagina_inicial(request):
    posts = Publicacao.objects.all().order_by('-data_criacao')
    return render(request, 'core/inicial.html', {'posts': posts})

def detalhe_post(request, post_id):
    post = get_object_or_404(Publicacao, id=post_id)
    if request.method == "POST":
        post.gostos += 1
        post.save()
        return redirect('detalhe_post', post_id=post.id)
    return render(request, 'core/detalhe.html', {'post': post})

def perfil_utilizador(request, username):
    utilizador = get_object_or_404(User, username=username)
    posts_utilizador = Publicacao.objects.filter(autor=utilizador)
    return render(request, 'core/perfil.html', {'utilizador': utilizador, 'posts': posts_utilizador})