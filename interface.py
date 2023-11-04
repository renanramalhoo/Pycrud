import os

#classe para interface do usuario

class Interface:
    #Construtor
    def __init__(self):
        pass

    def logotipo(self):
        print("-=-=-=-=-=-=-=-=-=-=")
        print("=-=-=-=FILMES-=-=-=-")
        print("-=-=-=-=-=-=-=-=-=-=")
        print("")

    def mostramenu(self):
        print("       Opções        ")
        print("1 - Cadastrar Filmes")
        print("2 - Lista de  Filmes")
        print("0 - Fechar  Programa")
        print("")

    def limpatela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #Permite ao usuario escolher uma opção
    # opcoes = []
    def selecionaopcao(self, opcoespermitidas = []):
        opcaoselecionada = input("Digite a opção desejada: ")

        # Verifica se digitou algo
        if opcaoselecionada == "":
            self.selecionaopcao()

        # Tenta converter em numero
        try:
            opcaoselecionada = int(opcaoselecionada)
        except ValueError:
            print("Opção Invalida!")
            return self.selecionaopcao()
        
        # Verifica se a opção selecionada é uma das opções validas
        if opcaoselecionada not in opcoespermitidas:
            print("Opção Invalida!")
            return self.selecionaopcao(opcoespermitidas)
        
        return opcaoselecionada
    
    def mostracadastrofilmes(self):
        self.logotipo()

        print("Insira os dados do filme: ")
        print("(campos com * são obrigatórios!)")

        titulo = self.solicitavalor('Digite o título: ', ['texto'], False)
        genero = self.solicitavalor('Digite o gênero: ', ['texto'], False)
        duracao = self.solicitavalor('Digite a duração: ', ['texto'], True)
        diretor = self.solicitavalor('Digite o diretor: ', ['texto'], True)
        estudio = self.solicitavalor('Digite o estúdio: ', ['texto'], True)
        classificacao = self.solicitavalor('Digite a classificação: ', ['texto'], True)
        ano = self.solicitavalor('Digite o ano: ', ['texto'], True)

    # Solicitar um valor do usuário e valida ele
    # return valordigitado
    def solicitavalor(self, valordigitado, tipo = ['texto', 'numero'], permiteNulo = False):

        # Verifica se digitou algo
        if valordigitado == "":
            self.solicitavalor()

        # Tenta converter em numero
        try:
            solicitavalor = int(valordigitado)
        except ValueError:
            print("Opção Invalida!")
            return self.selecionaopcao()
        
        return valordigitado