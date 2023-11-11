# Importa a classe Interface
from interface import Interface

# Classe principal do programa
interface = Interface()

opcao = ""
while opcao != 0:
    interface.logoTipo()
    interface.mostraMenu()
    opcao = interface.selecionaOpcao([1, 2, 0])
    interface.limpaTela()

    # Tela de cadastro de pneus
    if opcao == 1:
        interface.mostraCadastroPneus()
        opcao = ""
    # Tela de lista de pneus
    elif opcao == 2:
        interface.mostraLista()
        opcao = ""
        interface.limpaTela()