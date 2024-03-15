import sqlite3
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg, que geralmente está disponível
import matplotlib.pyplot as plt



class Email: # classe para enviar emails
    def __init__(self, email, senha): #metodo construtor
        self.email = email
        self.senha = senha

    def enviar(self, destinatario, conteudo):#metodo para enviar email
        smtp = smtplib.SMTP("smtp.gmail.com", 587) #criar um objeto smtp
        smtp.starttls()
        smtp.login(self.email, self.senha)

        message = MIMEMultipart()
        message["From"] = "Gestor de Projetos" #remetente
        message["To"] = destinatario #destinatario
        message["Subject"] = "Relatorio do Projeto e Tarefas" #assunto
        message.attach(MIMEText(conteudo, "plain"))

        smtp.sendmail(message["From"], message["To"], message.as_string()) #enviar email
        smtp.quit()

class ProjetoEnvio: # classe para enviar relatorios
    def __init__(self, email, nome, senha): #metodo construtor da classe ProjetoEnvio
        self.email = email
        self.nome = nome
        self.relatorios = []
        self.senha = senha

    def adicionar_relatorio(self, relatorio): #metodo para adicionar relatorios
        self.relatorios.append(relatorio)

    def enviar_relatorios(self): #metodo para enviar relatorios
        for relatorio in self.relatorios:
            relatorio.enviar_relatorio()

    def ler_dados(self, base_dados): #metodo para ler dados
        conn = sqlite3.connect(base_dados)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM projetos")
        dados_projetos = cursor.fetchall()

        cursor.execute("SELECT * FROM tarefas")
        dados_tarefas = cursor.fetchall()

        conn.close()

        conteudo_projetos = "\n".join(map(str, dados_projetos))
        conteudo_tarefas = "\n\n".join(map(str, dados_tarefas))

        conteudo = f"{conteudo_projetos}\n\n{conteudo_tarefas}"

        relatorio = Relatorio(conteudo, self)
        self.adicionar_relatorio(relatorio)

class Relatorio: # classe para gerar relatorios
    def __init__(self, conteudo, projeto_associado): #metodo construtor da classe Relatorio
        self.conteudo = conteudo
        self.data_criacao = datetime.datetime.now()
        self.projeto_associado = projeto_associado

    def enviar_relatorio(self): #metodo para enviar relatorio
        email = Email(self.projeto_associado.email, self.projeto_associado.senha)
        email.enviar(self.projeto_associado.email, self.conteudo)

if __name__ == "__main__": # metodo main
    email = "vfrango@gmail.com"
    senha = "usvr qxid jvdp qtvk"

    projeto = ProjetoEnvio(email, "Projeto de Teste", senha)
    base_dados = "1802925.db"
    projeto.ler_dados(base_dados)
    projeto.enviar_relatorios()

    print("Relatórios enviados com sucesso!")


class Dashboard:
    def __init__(self, base_dados):
        self.base_dados = base_dados

    def ler_dados(self):
        # Utiliza Pandas para ler dados diretamente em DataFrames
        self.dados_projetos = pd.read_sql_query("SELECT * FROM projetos", sqlite3.connect(self.base_dados))
        self.dados_tarefas = pd.read_sql_query("SELECT * FROM tarefas", sqlite3.connect(self.base_dados))

    def gerar_dashboard(self):
        if not self.dados_projetos.empty and not self.dados_tarefas.empty:
            plt.figure(figsize=(10, 6))
            sns.countplot(x='status', data=self.dados_projetos)
            plt.title('Distribuição de Projetos por Status')
            plt.show()

            plt.figure(figsize=(10, 6))
            sns.countplot(x='status', data=self.dados_tarefas)
            plt.title('Distribuição das tarefas por Status')
            plt.show()
        else:
            print("Não há dados suficientes para gerar o dashboard.")



"""""
    def mostrar_estatisticas(self):
        # check se os dados foram carregados
        if hasattr(self, 'dados_projetos') and not self.dados_projetos.empty:
            print("Estatísticas dos Projetos:")
            print(self.dados_projetos.describe())  # Descreve estatísticas básicas

            # Mostra gráficos 
            if 'coluna_exemplo' in self.dados_projetos.columns:
                plt.figure(figsize=(10, 6))
                sns.histplot(self.dados_projetos['satus'], kde=True)
                plt.title('Distribuição da Coluna status')
                plt.xlabel('Status')
                plt.ylabel('Frequência')
                plt.show()
            else:
                print("A coluna 'status' não foi encontrada nos dados dos projetos.")
        else:
            print("Dados dos projetos não estão disponíveis ou não foram carregados.")
            
"""

# Exemplo de uso
if __name__ == "__main__":
    dashboard = Dashboard("1802925.db")
    dashboard.ler_dados()
    dashboard.gerar_dashboard()
    ##dashboard.mostrar_estatisticas()
