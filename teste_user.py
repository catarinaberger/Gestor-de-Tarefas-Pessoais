from utilizador import Utilizador
from tarefa import Tarefa


# Criar um utilizador
utilizador = Utilizador("Catarina", "senha123")

# Testar criação de listas
utilizador.criar_lista("Trabalho")
utilizador.criar_lista("Estudos")
utilizador.criar_lista("Trabalho")  # Tentar criar uma lista duplicada

# Listar as listas criadas
print("\nListas atuais:")
for nome_lista in utilizador.listas:
    print(f"- {nome_lista}")

# Testar remoção de uma lista
utilizador.remover_lista("Trabalho")
utilizador.remover_lista("Viagem")  # Tentar remover uma lista inexistente

# Verificar as listas após remoção
print("\nListas atuais após remoção:")
for nome_lista in utilizador.listas:
    print(f"- {nome_lista}")
