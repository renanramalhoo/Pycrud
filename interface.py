import os
from bd import BD

#classe para interface do usuario

class Interface:
    #Construtor
    def __init__(self):
        self.banco = BD('catalogofilmes.db')

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

        titulo = self.solicitavalor('Digite o título * : ', 'texto', False)
        genero = self.solicitavalor('Digite o gênero * : ', 'texto', False)
        duracao = self.solicitavalor('Digite a duração: ', 'texto', True)
        diretor = self.solicitavalor('Digite o diretor: ', 'texto', True)
        estudio = self.solicitavalor('Digite o estúdio: ', 'texto', True)
        classificacao = self.solicitavalor('Digite a classificação * : ', 'texto', True)
        ano = self.solicitavalor('Digite o ano: ', 'numero', True)

        # Armazena os valores no banco de dados
        valores = {
            "titulo": titulo,
            "genero": genero,
            "duracao": duracao,
            "diretor": diretor,
            "estudio": estudio,
            "classificacao": classificacao,
            "ano": ano

        }
        self.banco.inserir('filmes')

    # Solicitar um valor do usuário e valida ele
    # return valordigitado
    def solicitavalor(self, legenda, tipo = ['texto', 'numero'], permiteNulo = False):
        valor = input(legenda)

        # Verifica se esta vazio
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitavalor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
            return valor
        
        if tipo == 'numero':
            try:
                valor = float(valor)
            except ValueError:
                print("Valor inválido!")
                return self.solicitavalor(legenda, tipo, permiteNulo)
            
        return valor