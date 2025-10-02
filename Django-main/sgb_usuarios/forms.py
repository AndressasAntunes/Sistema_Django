from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(
        label='Nome', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sobrenome = forms.CharField(
        label='Sobrenome', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_senha'})
    )
    confirmacao_senha = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    def clean(self):
        # 1. Chama a função clean do pai para garantir que os dados já foram limpos
        cleaned_data = super().clean()
        
        # 2. Obtém os valores dos campos
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        # 3. Verifica se os dois campos existem e se são diferentes
        if senha and confirmacao_senha and senha != confirmacao_senha:
            # 4. Se não coincidirem, lança um erro de validação
            raise forms.ValidationError(
                "As senhas digitadas não coincidem. Por favor, verifique."
            )
        return cleaned_data