import random
import string

def gerar_senha():
    tamanho_senha = 8
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho_senha))
    return senha

print("Sua nova senha é:", gerar_senha())