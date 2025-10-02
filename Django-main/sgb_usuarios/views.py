from .forms import CadastroForm 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.http import HttpResponse

def cadastra_usuario(request):
    if request.method == "POST":
        #  Cria uma instância do formulário, preenchendo-o com os dados do POST
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
            
            # Retorna uma resposta de sucesso ou redireciona
            # return HttpResponse('Usuário cadastrado com sucesso!') 
            return redirect('pagina_de_login') # Redireciona para a página de login

        else:
            # 6. Se o formulário não for válido, renderiza o template novamente
            # e envia o 'form' de volta para que os erros sejam exibidos.
            return render(request, "cadastro.html", {'form': form})
            
    else: 
        #cria um formulário vazio
        form = CadastroForm()
        
    return render(request, "cadastro.html", {'form': form})