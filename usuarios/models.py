from django.db import models
from datetime import datetime



class Usuarios(models.Model):
    
    OPCOES_GERENCIA = [
        
        ("MARIA ANGELICA", "Maria Angelica"),
        ("FLAVIA BRASIL", "Flavia Brasil"), 
        ("AGATHA TRINDADE", "Agatha Trindade"),
        
    ] 

    nome_usuario = models.CharField(max_length=50, null = False, blank=False)
    sobrenome_usuario = models.CharField(max_length=50, null = False, blank=False)
    matricula_usuario = models.CharField(max_length=7, null = False, blank=False, primary_key=True, unique=True)
    vertical_usuario = models.CharField(max_length=25, null=False, blank = False)
    gerencia_usuario = models.CharField(max_length=100, choices=OPCOES_GERENCIA, default="Escolha a sua Gerencia")
    email_usuario = models.EmailField(max_length=254, null = False, blank=False)
    senha_usuario = models.CharField(max_length=100, null = False, blank= False) 
    data_cadastro = models.DateTimeField(default= datetime.now, blank=False)
    
    
    
    def __str__(self):
        return self.nome_usuario
    
    
class HorasExtras(models.Model):
    
    MESES = [
        ("JANEIRO", "Janeiro"),
        ("FEVEREIRO", "Fevereiro"),
        ("MARÇO", "Março"),
        ("ABRIL", "Abril"),
        ("MAIO", "Maio"),
        ("JUNHO", "Junho"),
        ("JULHO", "Julho"),
        ("AGOSTO", "Agosto"),
        ("SETEMBRO", "Setembro"),
        ("OUTUBRO", "Outubro"),
        ("NOVEMBRO", "Novembro"),
        ("DEZEMBRO", "Dezembro")
    ]
    MOTIVOS = [
        ("RDM", "Rdm"),
        ("REPROCESSAMENTO", "Reprocessamento"),
        ("PROJETO", "Projeto"),
        ("OUTROS", "outros")
    ]
    
    matricula_usuario_hora_extra = models.CharField(max_length=7, null = False, blank=False)
    mes_hora_extra = models.CharField(max_length=20, choices= MESES, null = False, blank = False)
    horas_horas_extras = models.IntegerField(null = False, blank = False)
    minutos_horas_extras = models.IntegerField(null = False, blank = False)
    motivo_horas_extras = models.CharField(max_length=30, choices=MOTIVOS, null = False, blank = False)
    descricao_horas_extras = models.TextField(default = None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        
        return f"{self.matricula_usuario_hora_extra} - {self.mes_hora_extra}"
    