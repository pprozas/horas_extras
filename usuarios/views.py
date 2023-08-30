from django.shortcuts import render, redirect
from usuarios.forms import CadastroForms, LoginForms
from django.contrib import auth, messages
from usuarios.models import Usuarios

# Create your views here.

def index(request):
    
    return render(request, "usuarios/index.html")


def singup(request):
    
    form = CadastroForms()
    
    if request.method == "POST":
        
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            
            if form["senha_usuario"].value() != form["senha_confirma_usuario"].value():
                
                messages.error(request, "Erro ao confirmar a senha!")
                
                return redirect('singup')
        
            #Dando insert do usuario no banco de dados:
            
            nome_usuario = (form["nome_usuario"].value()).capitalize()
            sobrenome_usuario = (form["sobrenome_usuario"].value()).capitalize()
            matricula_usuario = form["matricula_usuario"].value()
            vertical_usuario = (form["vertical_usuario"].value()).capitalize()
            gerencia_usuario = (form["gerencia_usuario"].value()).capitalize()
            email_usuario = form["email_usuario"].value()
            senha_usuario = form["senha_usuario"].value()
            
                        
            if Usuarios.objects.filter(matricula_usuario = matricula_usuario).exists():
                
                messages.error(request,"Usuário já cadastrado! Por favor, faça o Login ao invés do SingUp")
                
                return redirect("singup") #Mudar para a pagina de login ao inves de ser mudar para singup
            
            
            novo_usuario = Usuarios.objects.create(
                
                nome_usuario = nome_usuario,
                sobrenome_usuario = sobrenome_usuario,
                matricula_usuario = matricula_usuario,
                vertical_usuario = vertical_usuario,
                gerencia_usuario = gerencia_usuario,
                email_usuario = email_usuario,
                senha_usuario = senha_usuario
                
                
            )
            
            novo_usuario.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            
            return redirect("index")
        

    return render(request, "usuarios/singup.html", {"forms":form})
            
            
                
                
                
def login(request):
    
    form = LoginForms()
    
    
    if request.method == "POST":
        
        form = LoginForms(request.POST)
        
        if form.is_valid():
            
            matricula_usuario = form["matricula_usuario"].value()
            senha_usuario = form["senha_usuario"].value()
            
            usuario_autenticado = Usuarios.objects.filter(matricula_usuario = matricula_usuario, senha_usuario = senha_usuario)
            
            if usuario_autenticado is not None:
                
                auth.login(request, usuario_autenticado)
                
                messages.success(request, "Logado com sucesso!")
                
                return redirect("index")
            
            else:
                
                
                messages.error(request, "Falha ao logar. Tente novamente.")
                
                return redirect("login")
    
    
    
    return render(request, "usuarios/login.html", {"forms":form})               
            
            
