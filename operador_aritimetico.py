nomeAluno = input('Qual o nome do aluno? ')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = ((nota1 + nota2 + nota3) / 3)

print(f'O aluno {nomeAluno} teve a média de {media:.2f}')
