from tarefa import Tarefa

class ListaDeTarefas:
    
    def __init__(self):
        self.tarefas = []
        
    #métodos ✨
    
    def adicionar_tarefa(self, tarefa):

        if any(tarefa.titulo == t.titulo for t in self.tarefas): #Para cada tarefa t na lista self.tarefas, a expressão verifica se o título da tarefa (tarefa.titulo) é igual ao título de t (t.titulo) e any retorna true
            print("Erro: já existe uma tarefa com este titulo!")
        else:
            self.tarefas.append(tarefa)
            print(f"A tarefa {tarefa.titulo} adicionada")
            
    def remover_tarefa(self, tarefa):
        
        if tarefa in self.tarefas:
            conf = input("Tem a certeza que quer remover esta tarefa? S/N: ").strip().upper()
            if conf == "S":
                self.tarefas.remove(tarefa)
                print(f"A tarefa {tarefa.titulo} foi removida! ")
            else:
                print(f"A tarefa {tarefa.titulo} permanece na lista.")
        else:
            print("Erro! Essa tarefa não foi encontrada.")
            
    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa) #Imprime o que formatei no __str__
        else:
            print("Nenhuma tarefa na lista.") 


'''
# Criando instâncias de tarefas
tarefa1 = Tarefa("Reunião de Projeto", "Alinhar objetivos do projeto", "2024-11-15", "Pendente", "Trabalho")

# Criando lista de tarefas


# Adicionando tarefas à lista
lista_tarefas.adicionar_tarefa(tarefa1)
lista_tarefas.adicionar_tarefa(tarefa2)
lista_tarefas.adicionar_tarefa(tarefa3)

# Remover uma tarefa existente
lista_tarefas.remover_tarefa(tarefa2)

# Listando as tarefas restantes
lista_tarefas.listar_tarefas()



    tarefa1 = Tarefa("Reunião de Projeto", "Alinhar objetivos do projeto", "2024-11-15", "Pendente", "Trabalho")
    lista_tarefas.adicionar_tarefa(tarefa1)
    lista_tarefas.remover_tarefa(tarefa2)
    lista_tarefas = ListaDeTarefas()''' 