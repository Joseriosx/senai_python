import random

def compararDoisValores(a, b):
    return a == b

def resultado():
    if compararDoisValores(numeroAleatório, numero):
        print('Acertou!! :(')
    else:
        print('errou!! :)')


numeroAleatório = random.randint(1,3)
numero = int(input('Informe um número entre 1 e 3: \n'))

print(resultado())

