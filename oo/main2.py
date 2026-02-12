from cliente import Cliente
from cliente import Cliente
from endereco import Endereco

def main():
    print("Inicializando Sistema")
    
    #Cliente N°1
    endereco = Endereco( "Av.Maranhão, 111 / ", "São joão / ", "Teresina / ", "PI")
    endereco2 = Endereco( "Av.São Luis, 111 / ", "São Sebastião / ", "Codó / ", "MA")
    
    cliente = Cliente('José', "Francisco")
    cliente.addEndereco(endereco)
    cliente.addEndereco(endereco2)
   
    #Cliente N°2
    print(f'Cliente: \nNome: {cliente.nomeCompleto()} ')
    print(f'Endereços: {cliente.visualizarEnderecos()}')

    endereco3 = Endereco( "Av.São Paulo, 666 / ", "São Pedro / ", "Teresina / ", "PI")
    endereco4 = Endereco( "Av.Barão de Gurgueia, 999 / ", "Vermelha / ", "Codó / ", "MA")
    

    cliente2 = Cliente('Marco', "Antonio")
    cliente2.addEndereco(endereco3)
    cliente2.addEndereco(endereco4)
   
    print(f'Cliente: \nNome: {cliente2.nomeCompleto()} ')
    print(f'Endereços: {cliente2.visualizarEnderecos()}')

    

if __name__ == "__main__":
    main()
