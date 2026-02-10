listaTupla = ('A', 'B', 'C') # Não altera
listaArray = ['A', 'B', 'C'] # Altera

print(listaArray[0]) 
listaArray[0] = 1
print(listaArray)

print(listaTupla[0])
listaTupla[0] = 1 #Erro, pois não altera
print(listaTupla)