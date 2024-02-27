from datetime import datetime

def obter_data_input(mensagem):
    # Função para obter a data do utilizador
    while True:
        try:
            data_str = input(mensagem)
            data = datetime.strptime(data_str, "%Y-%m-%d")
            return data
        except ValueError:
            print("Formato de data incorreto. Por favor, use o formato YYYY-MM-DD.")

class Projeto:
    def __init__(self, id_projeto, nome, descricao, data_inicio, data_termino, status):
        # Inicializa um novo projeto com os atributos fornecidos
        self.id_projeto = id_projeto
        self.nome = nome
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.status = status
        self.tarefas = []

    def adicionar_tarefa(self):
        # Método para adicionar uma nova tarefa ao projeto
        tarefa_id = input("Escreva o ID da tarefa: ")
        descricao = input("Escreva a descrição da tarefa: ")
        data_inicio = obter_data_input("Escreva a data de início da tarefa (formato YYYY-MM-DD): ")
        data_fim_prevista = obter_data_input("Escreva a data de término prevista da tarefa (formato YYYY-MM-DD): ")
        status = "Atribuída"

        nova_tarefa = Tarefa(tarefa_id, descricao, data_inicio, data_fim_prevista, status)
        self.tarefas.append(nova_tarefa)

    def alterar_status(self, novo_status):
        # Método para alterar o status do projeto
        self.status = novo_status

    def obter_informacoes(self):
        # Método para obter informações sobre o projeto e suas tarefas
        informacoes_projeto = f"ID: {self.id_projeto}, Nome: {self.nome}, Status: {self.status}"
        if not self.tarefas:
            return f"{informacoes_projeto}\nO projeto não possui tarefas no momento."
        else:
            informacoes_tarefas = "\n".join([tarefa.obter_informacoes() for tarefa in self.tarefas])
            return f"{informacoes_projeto}\nInformações das Tarefas:\n{informacoes_tarefas}"

    def __str__(self):
        # Método para retornar uma representação em string do projeto
        return f"ID: {self.id_projeto}, Nome: {self.nome}, Status: {self.status}"

    def finalizar_projeto(self):
        # Método para finalizar o projeto
        self.status = "Concluído"
        self.data_termino = datetime.now().strftime("%Y-%m-%d")

    def listar_tarefas_concluidas(self):
        # Método para listar as tarefas concluídas do projeto
        return [tarefa for tarefa in self.tarefas if tarefa.status == "Concluída"]

class Tarefa:
    def __init__(self, tarefa_id, descricao, data_inicio, data_fim_prevista, status):
        # Inicializa uma nova tarefa com os atributos fornecidos
        self.tarefa_id = tarefa_id
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim_prevista = data_fim_prevista
        self.status = status
        self.responsavel = None

    def atribuir_responsavel(self, responsavel):
        # Método para atribuir um responsável à tarefa
        self.responsavel = responsavel

    def alterar_status(self, novo_status):
        # Método para alterar o status da tarefa
        self.status = novo_status

    def obter_informacoes(self):
        # Método para obter informações sobre a tarefa
        return f"ID: {self.tarefa_id}, Descrição: {self.descricao}, Status: {self.status}"


class Equipa:
    def __init__(self, equipa_id, nome):
        # Inicializa uma nova equipa com os atributos fornecidos
        self.equipa_id = equipa_id
        self.nome = nome
        self.membros = []  # Lista para armazenar os membros da equipe

    def adicionar_membro(self, membro):
        # Método para adicionar um novo membro à equipa
        self.membros.append(membro)


    def remover_membro(self, membro):
        # Método para remover um membro da equipa
      self.membros.remove(membro)

    def listar_membros(self):
        # Método para listar os membros da equipa
        return [membro for membro in self.membros]


class Membro:
    def __init__(self, membro_id, nome, cargo, competencias):
        # Inicializa um novo membro com os atributos fornecidos
        self.membro_id = membro_id
        self.nome = nome
        self.cargo = cargo
        self.competencias = competencias
        self.tarefas_atribuidas = []  # Lista para armazenar as tarefas atribuídas ao membro

    def atualizar_competencias(self, novas_competencias):
        # Método para atualizar as competências do membro
        self.competencias = novas_competencias

    def atribuir_tarefa(self, tarefa):
        # Método para atribuir uma tarefa ao membro
        self.tarefas_atribuidas.append(tarefa)

    def verificar_disponibilidade(self):
        # Método para verificar se o membro está disponível (não tem tarefas atribuídas)
        return len(self.tarefas_atribuidas) == 0



class Cliente:
    def __init__(self, cliente_id, nome, empresa, projetos_anteriores):
        self.cliente_id = cliente_id
        self.nome = nome
        self.empresa = empresa
        self.projetos_anteriores = projetos_anteriores

    def solicitar_novo_projeto(self, projeto):
        # Lógica para processar solicitação de novo projeto
        self.projetos_anteriores.append(projeto)

    def visualizar_projetos_atuais(self):
        # Lógica para exibir projetos atuais
        self.projetos_atuais = []

    def fornecer_feedback(self, feedback):
        # Lógica para processar feedback do cliente
        self.feedback = feedback


class Relatorio:
    def __init__(self, relatorio_id, conteudo, projeto_associado):
        # Inicializa um novo relatório com os atributos fornecidos
        self.relatorio_id = relatorio_id
        self.conteudo = conteudo
        self.data_criacao = datetime.now()
        self.projeto_associado = projeto_associado

    def adicionar_ao_projeto(self, projeto):
        # Método para adicionar o relatório a um projeto
        pass

    def visualizar_relatorio(self):
        # Método para visualizar o relatório
        pass


class Calendario:
    def __init__(self):
        # Inicializa um novo calendário
        self.feriados = []
        self.prazos_projeto = []

    def adicionar_feriado(self, data):
        # Método para adicionar um feriado ao calendário
        pass

    def adicionar_prazo_projeto(self, data):
        # Método para adicionar um prazo de projeto ao calendário
        pass

    def verificar_disponibilidade(self, data):
        # Método para verificar a disponibilidade de uma data no calendário
        pass


class Departamento:
    def __init__(self, departamento_id, nome):
        # Inicializa um novo departamento com os atributos fornecidos
        self.departamento_id = departamento_id
        self.nome = nome
        self.projetos_atuais = []
        self.membros = []

    def atribuir_projeto(self, projeto):
        # Método para atribuir um projeto ao departamento
        pass

    def adicionar_membro(self, membro):
        # Método para adicionar um membro ao departamento
        pass

    def remover_membro(self, membro):
        # Método para remover um membro do departamento
        pass



class Notificacao:
    def __init__(self, notificacao_id, conteudo, destinatario):
        # Inicializa uma nova notificação com os atributos fornecidos
        self.notificacao_id = notificacao_id
        self.conteudo = conteudo
        self.destinatario = destinatario
        self.data_envio = datetime.now()

    def enviar_notificacao(self):
        # Método para enviar a notificação
        pass

    def marcar_como_lida(self):
        # Método para marcar a notificação como lida
        pass

    def excluir_notificacao(self):
        # Método para excluir a notificação
        pass


# Exemplo de utilização
projeto = Projeto("1", "Projeto Teste", "Descrição do Projeto", "2023-01-01", "2023-12-31", "Em Andamento")
projeto.adicionar_tarefa()  # Chama diretamente a função adicionar_tarefa no objeto do projeto
print(projeto.obter_informacoes())

