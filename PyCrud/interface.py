import os
from db import DB

# Classe para interface do usuário do programa

class Interface:
        # construtor
        def __init__(self):
                self.banco = DB("catalogoPneus.db")

        def logoTipo(self): #self representa a própria classe
                print()
                print("================================")
                print("====== Catálogo de Pneus  ======")
                print("================================")
                print()
        
        def limpaTela(self):
                os.system('cls' if os.name == 'nt' else 'clear')

        # Função que permite o usuário escolher uma opção
        # opcoes = []
        def selecionaOpcao(self, opcoesPermitidas = []):
                
                opcaoSelecionada = input("Digite a opção desejada: ")

                # Verifica se digitou algo
                if opcaoSelecionada == "":
                        return self.selecionaOpcao(opcoesPermitidas) # recursividade (chama a própria função)
                
                # Tenta converter para número
                try:
                        opcaoSelecionada = int(opcaoSelecionada)
                except ValueError:
                        print("Opção inválida")
                        return self.selecionaOpcao(opcoesPermitidas)
                
                # Verifica se a opção selecionada é válida
                if opcaoSelecionada not in opcoesPermitidas:
                        print("Opção inválida")
                        return self.selecionaOpcao(opcoesPermitidas)

                # Retorna o valor selecionado pelo usuário
                return opcaoSelecionada
        
        # Mostra menu principal do sistema
        def mostraMenu(self):
                print("1 - Cadastrar Pneu")
                print("2 - Listar Pneus")
                print("0 - Sair")
                print()

        # Mostra a Tela de Cadastro de Pneus
        def mostraCadastroPneus(self):
                self.logoTipo()

                print ("Insira os dados do pneu:")
                print ("(Campos com * são obrigatórios)")
                print()

                marca = self.solicitaValor('Digite a marca (*): ', 'texto', False)
                altura = self.solicitaValor('Digite a altura (*): ', 'texto', False)
                largura = self.solicitaValor('Digite a largura (*): ', 'texto', False)
                aro = self.solicitaValor('Digite o aro (*): ', 'texto', False)

                # Armazena os valores no Banco de Dados
                valores = {
                        "marca" : marca,
	                "altura" : altura,
                        "largura" : largura,
                        "aro" : aro,}
                self.banco.inserir('pneus', valores)
                

        # Solicita um valor do usuário e valida ele
        def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
                valor = input(legenda)

                # Verifica se está vazio
                if valor == "" and not permiteNulo:
                        print("Valor inválido")
                        return self.solicitaValor(legenda, tipo, permiteNulo)
                elif valor == "" and permiteNulo:
                        return valor
                
                # Verifica se está no tipo correto
                if tipo == 'numero':
                        try:
                                valor = float(valor)
                        except ValueError:
                                print("Valor inválido")
                                return self.solicitaValor(legenda, tipo, permiteNulo)

                return valor
        
        def mostraLista (self):
                self.logoTipo()
                print("Veja abaixo a lista de pneus cadastrados")
                print()

                pneus = self.banco.buscaDados('pneus')

                for pneu in pneus:
                        id, marca, altura, largura, aro = pneu
                        print(f"Pneu {id} - {marca} - {altura} | {largura} | R{aro}")
                
                print()
                input("Tecle Enter para voltar ao Menu principal")
                self.limpaTela()
                self.mostraMenu()

