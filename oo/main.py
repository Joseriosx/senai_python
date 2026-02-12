from veiculo import Veiculo
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

def main():
    print('Inicializando sistema!')
    list = []

    jose = PessoaFisica('José Henrique', '86 9.999.999', 'Rua dos Ipes', '666.666.666-66')
    senai = PessoaJuridica('Senai', '86 9.666.666', 'Teresina Shopping', '12323434556')

    list.append(jose)
    list.append(senai)

    for p in list:
        print(f'{p.exibir_dados()}')

if __name__ == "__main__":
    main()





def main():
    print('Inicializando sistema!')
    lista = []

    carroByd = Veiculo(2026, 'BYD', 4)
    motoHonda = Veiculo(2026, 'HONDA', 2)

    lista.append(carroByd)
    lista.append(motoHonda)

    for v in lista:
        print(f'{v.marca}')

if __name__ == "__main__":
    main()
