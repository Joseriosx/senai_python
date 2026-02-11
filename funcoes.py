'''
def soma(a, b):
    return a + b
    

resultado = soma(1, 2)
print(f'Resultado 1: {resultado}')

print(soma(1, 2))

x = 1
y = 2

resultado2 = soma(x, y)
print(f'Resultado 2: {resultado2}')

def subtracao(a, b):
    return a - b

x = 1
y = 2

resultado3 = subtracao(x, y)
print(f'Resultado da subtração: {resultado3}')
'''
def semRetorno(): #VOID
    print('Não tenho retorno')

print(semRetorno())

def nomeCompleto(primeiroNome, segundoNome):
    return primeiroNome + ' ' + segundoNome

primeiroNome = input('Informe seu primeiro nome: ')
segundoNome = input('Informe seu segundo nome: ')

nome = nomeCompleto(primeiroNome, segundoNome)

print('Seu nome completo é', nome)
