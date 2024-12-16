class Tarefa:

    def __init__(self, titulo, desc, data, status, categ):
        self.titulo = titulo
        self.desc = desc
        self.data = data
        self.status = "pendente" #começa sempre pendente 
        self.categ = categ


    def gerir_status (self):
        
        tarefa_concluida = (input("Concluiu a tarefa? S ou N: ")).strip().upper()

        if tarefa_concluida == "S":
            self.status = "concluída"
            print(f"A tarefa {self.titulo} foi {self.status}!")
        elif tarefa_concluida == "N": #só é verificado se o de cima for falso
            print(f"A tarefa {self.titulo} continuará como {self.status}.")
        else:
            print("Erro. Escreva 'S' para sim ou 'N' para não.")

    def __str__(self):
        return f"Título: {self.titulo}, Descrição: {self.desc}, Data: {self.data}, Categoria: {self.categ}, Status: {self.status}"



           
       