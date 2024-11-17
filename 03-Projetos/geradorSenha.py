import random
import string

def gerar_senha(tamanho=12):
    """Função para gerar uma senha aleatória de tamanho especificado"""
    
    # Definindo os caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gerando a senha aleatória
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Definindo o tamanho da senha
tamanho = 16

# Gerando e exibindo a senha
senha_gerada = gerar_senha(tamanho)
print("Sua senha gerada é:", senha_gerada)
