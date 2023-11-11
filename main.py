#Importa a classe interface
from interface import Interface
from bd import BD

#Classe principal do programa
interface = Interface()


#Variaveis
opcao = ""

#Loop Principal
while opcao != 0:
    interface.logotipo()
    interface.mostramenu()
    opcao = interface.selecionaopcao([1, 2, 0])
    interface.limpatela()
    
    # Tela de cadastro de filmes
    if opcao == 1:
        interface.mostracadastrofilmes()

    # Tela de lista de filmes
    if opcao == 2:
        pass
    