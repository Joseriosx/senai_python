salario = float(input('informe o salário: '))
porcentagem = float(input('Informe a porcentagem de aumento: '))
resultado = salario + (salario * (porcentagem / 100))

print(f'O salário será de {resultado:.2f}')

