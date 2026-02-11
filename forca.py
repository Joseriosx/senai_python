continuar = True #Condição para while
palavraChave = input(f'Informe uma palavra: \n').lower().strip() #Palavra a ser advinhada

digitadas = []
acertos = []
erros = 0

while continuar:

    senha = ""

    for letra in palavraChave:
        senha += letra if letra in acertos else "."

    print(senha)

    if senha == palavraChave:
        print('Você acertou!')
        opcao = int(input('Deseja continuar? 1-sim | 2-não \n'))
        if opcao == 2:
            continuar = False

    tentativa = input('Digite uma letra: \n').lower().strip()

    if tentativa in digitadas:
        print('Você já digitou esta letra')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavraChave:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')

    print('X==:==\nX : ')
    print('X O ' if erros >= 1 else 'X') #Cabeça do boneco
    linha2 = ""
    if erros == 2: #braços e tronco
        linha2 += " | "
    elif erros == 3:
        linha2 += " |/ " 
    elif erros >= 4:
        linha2 += '\|/ '

    print('X%s' % linha2)

    linha3 = '' 
    if erros == 5: #Pernas do boneco
        linha3 += '/ '
    elif erros >= 6:
        linha3 += '/ \ '

    print('X%s' % linha3)
    print('X\n============')

    if erros == 6: #Perdeu
        print('Enforcado!! :( ')
        