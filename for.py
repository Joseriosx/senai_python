lista = ('Morango', 'Pera', 'Uva', 'Banana')

print('Usando FOR')
for frutas in lista:
    print(frutas)

#for(x = 0; x < lista.length(); x++) {
#
#}

print('Usando WHILE')
count = 0

while count < len(lista):
    print(lista[count])
    count = count + 1