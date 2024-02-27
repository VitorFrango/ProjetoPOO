import sqlite3
from datetime import datetime  # importa a biblioteca datetime

from basedados import Basedados  # importa a classe basedados
from tarefa import Tarefa  # importa a classe tarefa


class Trabalhos:  # classe atividade  com os atributos descricao, data_inicio, data_fim_prevista e status

    def __init__(self, descricao, data_inicio, data_fim_prevista, status):  # construtor da classe atividade
        self.descricao = descricao
        self.responsavel = None
        self.data_inicio = data_inicio
        self.data_fim_prevista = data_fim_prevista
        self.status = status

    def obter_informacoes(self):  # obter informações da atividade
        return (f"Descrição: {self.descricao}, Status: {self.status}, Início: {self.data_inicio}, "
                f"Previsto Fim: {self.data_fim_prevista}")


class Tarefa(Trabalhos):
    def __init__(self, id_projeto, descricao, responsavel, data_inicio, data_fim_prevista, status):
        super().__init__(descricao, data_inicio, data_fim_prevista, status)
        self.id_projeto = id_projeto
        self.responsavel = responsavel

class Projeto(Trabalhos):
    basedados = Basedados()  # instanciar a classe basedados

    def set_basedados(cls, basedados, self=None):  # construtor da classe projeto
        self.basedados = basedados()

    def __init__(self, id_projeto, nome, descricao, data_inicio, data_fim_prevista, status):
        super().__init__(descricao, data_inicio, data_fim_prevista, status)
        self.id_projeto = id_projeto
        self.nome = nome

    @classmethod
    def adicionar_projeto(cls):
        id_projeto = input("Escreva o ID do projeto: ")
        nome = input("Escreva o nome do projeto: ")
        descricao = input("Escreva a descrição do projeto: ")
        data_inicio = obter_data_input("Escreva a data de início do projeto (formato YYYY-MM-DD): ")
        data_fim_prevista = obter_data_input("Escreva a data de término prevista do projeto (formato YYYY-MM-DD): ")
        status = "Em Andamento"

        novo_projeto = Projeto(id_projeto, nome, descricao, data_inicio, data_fim_prevista, status)
        cls.basedados.adicionar_projeto(novo_projeto)


    @classmethod
    @classmethod
    def adicionar_tarefa(cls):
        try:
            id_projeto = input("Escreva o ID do projeto: ")
            descricao = input("Escreva a descrição da tarefa: ")
            responsavel = input("Escreva o nome do responsável pela tarefa: ")
            data_inicio = input("Escreva a data de início da tarefa: ")
            data_fim_prevista = input("Escreva a data prevista para o fim da tarefa: ")
            status = input("Escreva o status da tarefa: ")
            nova_tarefa = Tarefa(id_projeto, descricao, responsavel, data_inicio, data_fim_prevista, status)
            cls.basedados.adicionar_tarefa(nova_tarefa)  # Adicionar a tarefa a base de dados
            return nova_tarefa
        except sqlite3.IntegrityError:
            print("The task could not be added because it references a record that does not exist.")
def obter_informacoes(self):  # obter informações do projeto
    informacoes_projeto = f"ID Projeto: {self.id_projeto}, Nome: {self.nome}, {super().obter_informacoes()}"
    if not self.tarefas:
        return f"{informacoes_projeto}\nO projeto não possui tarefas no momento."
    else:
        informacoes_tarefas = "\n".join([tarefa.obter_informacoes() for tarefa in self.tarefas])
        return f"{informacoes_projeto}\nInformações das Tarefas:\n{informacoes_tarefas}"
    cls.basedados.obter_informacoes()  # Obter informações do projeto


def finalizar_projeto(self):  # finalizar projeto
    self.status = "Concluído"
    self.data_fim_prevista = datetime.now().strftime("%Y-%m-%d")

    def listar_tarefas_concluidas(self):  # listar tarefas concluidas
        return [tarefa for tarefa in self.tarefas if tarefa.status == "Concluída"]


def obter_data_input(mensagem):  # obter data de input
    while True:
        try:
            data_str = input(mensagem)
            data = datetime.strptime(data_str, "%Y-%m-%d")
            return data
        except ValueError:
            print("Formato de data incorreto. Por favor, use o formato YYYY-MM-DD.")
