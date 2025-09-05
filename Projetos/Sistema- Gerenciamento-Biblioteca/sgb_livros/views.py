from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def livros(request):
    #return HttpResponse('Olá mundo')
    return render(request,'livros.html')

def salva_livros(request):
    titulo_livro = request.POST['titulo_livro']
    autor_livro = request.POST["autor_livros"]
    editora_livro = request.POST['editora_livros']
    return render(request, 'livros.html', context={'titulo_livro':titulo_livro})
    #return HttpResponse('Livro salvo'+ titulo_livro)