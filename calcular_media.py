contador = 0
notas = []

def media(lista):
    total = 0
    for i in lista:
        total = total + i
    return total / len(lista)

while contador < 3:
    contador += 1
    nota = float(input(f'Informe a {contador}° nota: '))
    notas.append(nota)

print('Notas: ' ,notas)

resultado = media(notas)
print(f'Resultado: {resultado}')