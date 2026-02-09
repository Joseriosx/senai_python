nomeAluno = input('Qual o nome do aluno? ')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = ((nota1 + nota2 + nota3) / 3)
situacao = ''
#Se o aluno tiver a média igual ou maior que 7 - Aprovado
#Se o aluno tiver a média entre 5 a 7 - Recuperação
#Se o aluno tiver a média abaixo de 5 - Reprovado 

if media >= 7:
    situacao = 'aprovado'
elif media >=5 and media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'reprovado'

print(f'O aluno {nomeAluno} obteve a média de {media:.2f} e está {situacao}.')