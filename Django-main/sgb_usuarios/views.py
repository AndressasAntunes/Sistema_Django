from .forms import CadastroForm 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from sgb_livros.models import Livro

def cadastra_usuario(request):
    sucesso = False  # Variável para controlar a mensagem de sucesso
    
    if request.method == "POST":
        # Cria uma instância do formulário, preenchendo-o com os dados do POST
        form = CadastroForm(request.POST) 
        
        # Verifica se os dados são válidos 
        if form.is_valid():
            
            # Acessa os dados limpos e validados 
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha'] 
            
            username_candidato = email 
            
            # Verifica se o usuário já existe
            if User.objects.filter(username=username_candidato).exists():
                return HttpResponse('Usuário já existe!', status=409) # 409 Conflict

            # Cria o usuário e HASH a senha
            user = User.objects.create_user(
                username=username_candidato,
                email=email,
                password=senha, # O create_user já faz o hash da senha
                first_name=nome,
                last_name=sobrenome
            )
            
            # Define sucesso como True e limpa o formulário
            sucesso = True
            form = CadastroForm()  # Limpa o formulário após cadastro bem-sucedido
            
            # Renderiza a mesma página com a mensagem de sucesso
            return render(request, "cadastro.html", {'form': form, 'sucesso': sucesso})

        else:
            # Se o formulário não for válido, renderiza o template novamente
            # e envia o 'form' de volta para que os erros sejam exibidos.
            return render(request, "cadastro.html", {'form': form})
            
    else: 
        # cria um formulário vazio
        form = CadastroForm()
        
    return render(request, "cadastro.html", {'form': form, 'sucesso': sucesso})

def loga_usuario(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else: 
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']

        usuario = authenticate(username=nome_usuario, password=senha)

        if usuario: 
            login(request, usuario)
            livros = Livro.objects.all()
            return render(request, 'livros.html', {'livros': livros})
        else:
            return HttpResponse('Usuário e/ou senha inválidos!')
        
def logout_usuario(request):
    logout(request)
    return render(request, 'login.html')