from django import forms


class CadastroForms(forms.Form):
    
    OPCOES_GERENCIA = [
        
        ("MARIA ANGELICA", "Maria Angelica"),
        ("FLAVIA BRASIL", "Flavia Brasil"), 
        ("AGATHA TRINDADE", "Agatha Trindade"),
        
    ]
    
    nome_usuario = forms.CharField(
        label = "Nome",
        required= True,
        max_length=100,
        label_suffix= "alinhado1",
        widget= forms.TextInput(
            
            attrs = {
                "class": "form-control",
                "placeholder": "Ex: Pedro"
            }
        )
    )
    
    sobrenome_usuario = forms.CharField(
        
        label = "Sobrenome",
        required=True,
        max_length=100,
        label_suffix= "alinhado1",
        widget=forms.TextInput(
            
            attrs= {
                "class": "form-control",
                "placeholder": "Ex: 'da Silva' OU 'Henrique' "
            }
        )
    )
    
    matricula_usuario = forms.CharField(
        
        label = "Matrícula", 
        required= True,
        max_length=9,
        label_suffix= "alinhado2",
        widget= forms.TextInput(
            
            attrs={
                "class": "form-control",
                "placeholder": "Ex: 9421120"
            }
        )
    )
    
    vertical_usuario = forms.CharField(
        
        label = "Vertical",
        required=True,
        max_length=25,
        label_suffix= "alinhado2",
        widget= forms.TextInput(
            
            attrs={
                "class": "form-control",
                "placeholder":"Ex: BARE ou DGDS"
            }
        )
    )
    
    gerencia_usuario = forms.ChoiceField(
        
        label = "Gerência:",
        required=True,
        choices=OPCOES_GERENCIA,
        label_suffix= "alinhado3",
        widget= forms.Select(
            
            attrs= {
                
                "class": "form-control",
                "placeholder": "Selecione uma das opções"
            }
        )
    )
    
    email_usuario = forms.EmailField(
        
        label = "Email",
        required=True, 
        max_length=100,
        label_suffix= "alinhado4",
        widget= forms.EmailInput(
            
            attrs = {
                
                "class": "form-control",
                "placeholder":  "Ex: pepe_rosas@dominio.com.br"
            }
        )
    )
    
    senha_usuario = forms.CharField(
        
        label = "Senha",
        required=True,
        max_length=50,
        label_suffix= "alinhado5",
        widget=forms.PasswordInput(
            
            attrs = {
                
                "class": "form-control",
                "placeholder": "Digite a sua Senha"
            }
        )
    )
    
    senha_confirma_usuario = forms.CharField(
        
        label = "Confirme sua Senha",
        required=True,
        max_length=50,
        label_suffix= "alinhado5",
        widget= forms.PasswordInput(
            
            attrs= {
                
                "class": "form-control",
                "placeholder":"Confirme sua Senha."
            }
        )
    )
    

            
            
class LoginForms(forms.Form):
    
    matricula_usuario = forms.CharField(
        
        label = "Matrícula",
        required=True,
        max_length=9,
        widget= forms.TextInput(
            
            attrs={
                "class": "form-control",
                "placeholder": "Ex: 9123456"
            }
        )
    )
    
    
    senha_usuario = forms.CharField(
        
        label = "Senha",
        required=True,
        max_length=50,
        widget= forms.PasswordInput(
            
            attrs={
                "class": "form-control", 
                "placeholder": "Digite a sua Senha"
            }
        )
    )
    