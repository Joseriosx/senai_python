tabelas = {
    'Abacaxi' : 4.5,
    'Pera' : 6.,
    'Uva' : 18.5,
    'Melancia' : 3.5
}

#Imprime a lista
print(tabelas)

#Imprime somente as chaves
print(tabelas.keys())

#Imprime somente os valores
print(tabelas.values())

#Imprimir valor específico
print(tabelas['Abacaxi'])

tabelas.update({
    'Melão': 5.35,
    'Banana': 7.99,
})

print(f'Atualizar tabela:\n{tabelas}')

tabelas.update({
    'Uva': 10.5
})
tabelas.setdefault('Manga', 11.)

print(f'Atualizar tabela:\n{tabelas}')