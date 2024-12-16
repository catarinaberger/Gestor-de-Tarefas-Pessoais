from lista_de_tarefas import ListaDeTarefas
from tarefa import Tarefa

# Criando uma instância da lista de tarefas
lista_tarefas = ListaDeTarefas()

# Criando algumas instâncias de Tarefa
tarefa1 = Tarefa("Reunião de Projeto", "Alinhar objetivos do projeto", "2024-11-15", "Pendente", "Trabalho")
tarefa2 = Tarefa("Estudo para prova", "Estudar matemática", "2024-11-16", "Pendente", "Estudos")
tarefa3 = Tarefa("Reunião de Projeto", "Reunião de planeamento", "2024-11-17", "Pendente", "Trabalho")  # Título duplicado

# Teste 1: Adicionar tarefas
print("Adicionando tarefas:")
lista_tarefas.adicionar_tarefa(tarefa1)
lista_tarefas.adicionar_tarefa(tarefa2)
lista_tarefas.adicionar_tarefa(tarefa3)  # Esta tarefa não será adicionada

# Teste 2: Listar tarefas após adição
print("\nLista de tarefas após adição:")
lista_tarefas.listar_tarefas()

# Teste 3: Remover tarefa existente
print("\nA remover a tarefa 'Estudo para o Teste':")
lista_tarefas.remover_tarefa(tarefa2)

# Teste 4: Listar tarefas após remoção
print("\nTarefas após remoção:")
lista_tarefas.listar_tarefas()

# Teste 5: Tentar remover tarefa que não existe
print("\nTentar remover uma tarefa inexistente:")
tarefa_inexistente = Tarefa("Viagem de férias", "Viajar para a praia", "2024-12-01", "Pendente", "Pessoal")
lista_tarefas.remover_tarefa(tarefa_inexistente)
