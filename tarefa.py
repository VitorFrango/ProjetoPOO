class Atividade:
    def __init__(self, id_tarefa, id_projeto, descricao, data_inicio, data_fim_prevista, status):
        self.id_tarefa = id_tarefa
        self.id_projeto = id_projeto
        self.responsavel = None
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim_prevista = data_fim_prevista
        self.status = status

    def obter_informacoes(self):
        return (
            f"ID Tarefa: {self.id_tarefa}, ID Projeto: {self.id_projeto}, Descrição: {self.descricao}, "
            f"Início: {self.data_inicio}, Previsto Fim: {self.data_fim_prevista}, Status: {self.status} "
        )


class Tarefa(Atividade):
    def __init__(self, tarefa=None, id_projeto=None, descricao=None, data_inicio=None, data_fim_prevista=None,
                 responsavel=None, nome_projeto=None, status=None):
        super().__init__(tarefa, id_projeto, descricao, data_inicio, data_fim_prevista, status)
        self.responsavel = responsavel
        self.nome_projeto = nome_projeto

    def obter_informacoes(self):
        return (
            f"ID Tarefa: {self.id_tarefa}, ID Projeto: {self.id_projeto}, Descrição: {self.descricao}, "
            f"Status: {self.status}, Início: {self.data_inicio}, Previsto Fim: {self.data_fim_prevista}, "
            f"Responsável: {self.responsavel}"
        )

    def alterar_status(self):
        print(f"QUal a tarera que deseja alterar o status?")
        id_tarefa = input("Escreva o ID da tarefa: ")
        novo_status = input("Escreva o novo status: ")
        self.status = novo_status
        print(f"O status da tarefa {id_tarefa} foi alterado para {self.status}.")
        return self

    def atribuir_responsavel(self):
        print(f"Qual a tarefa que deseja atribuir um responsável?")
        tarefa = input("Escreva o ID da tarefa: ")
        responsavel = input("Escreva o nome do responsável: ")
        self.responsavel = responsavel
        print(f"O responsável pela tarefa {tarefa} foi alterado para {self.responsavel}.")
        return self