from lista_de_tarefas import ListaDeTarefas

class Utilizador:

    def __init__(self, nome, password):
        self.nome = nome
        self.__password = password
        self.listas = {} #isto é um dicionário, organiza informações de forma que seja fácil aceder por meio de uma chave única 
    
    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def criar_lista(self, nome_lista):
        if nome_lista in self.listas:
            print(f"Erro! Já existe uma lista chamada {nome_lista}.")
        else:
            self.listas[nome_lista] = ListaDeTarefas()
            print(f"A lista {nome_lista} foi criada!")
    
    def remover_lista(self, nome_lista):
        if nome_lista in self.listas:
            conf = (input("Tem a certeza que quer remover esta lista? S/N")).strip().upper()
            if conf == "S":
                del self.listas[nome_lista]
                print(f"A lista {nome_lista} foi removida.")
            else:
                print(f"A {nome_lista} permanece na lista.")
        else:
            print(f"A lista {nome_lista} não foi encontrada.")