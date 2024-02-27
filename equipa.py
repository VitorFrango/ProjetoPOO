from basedados import Basedados

class Equipa:
    basedados = Basedados()  # Add this line if 'basedados' is supposed to be an attribute

    def set_basedados(cls, basedados, self=None):  # construtor da classe projeto
        self.basedados = basedados()
    def __init__(self, id_equipa=None, nome=None, tarefa=None):
        self.id_equipa = id_equipa
        self.nome = nome
        self.tarefa = tarefa
        self.membros = []

    def adicionar_membro(self):
        id_membro = input("Escreva o ID: ")
        tarefa = input("Escreva o ID da tarefa: ")
        nome = input("Escreva o nome do membro: ")
        cargo = input("Qual o cargo: ")
        competencias = input("Quais as competências: ")
        membro = Membro(id_membro, tarefa, nome, cargo, competencias)
        self.membros.append(membro)
        self.basedados.adicionar_membro(membro)  # Inserir membro na base de dados


class Membro:
    def __init__(self, id_membro, nome, cargo, competencias,tarefa):
        self.id_membro = id_membro
        self.nome = nome
        self.cargo = cargo
        self.competencias = competencias
        self.tarefa = tarefa
        self.tarefas_atribuidas = []

    def atualizar_competencias(self, novas_competencias=None):
        if novas_competencias is None:
            novas_competencias = input("Escreva a nova competência do membro: ")
        self.competencias = novas_competencias
        print(f"A competência foi alterada para {self.competencias}.")
