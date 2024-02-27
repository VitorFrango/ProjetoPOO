import sys

from basedados import Basedados
from equipa import Equipa
from projeto import  Projeto
from projeto import Tarefa
from tarefa import Tarefa
from relatorio import ProjetoEnvio
from relatorio import Dashboard


class MenuPrincipal:  # classe menu principal
    def exibir_menu(self):  # definição do menu principal
        print("""
        -----------------------------
        Gestão de Projetos e Tarefas
        -----------------------------
        1-  Criar um projeto
        2-  Adicionar tarefas a um projeto 
        3-  Atribuir responsáveis a tarefas
        4-  Alterar estado de tarefas 
        5-  Consultar estado das tarefas
        6-  Adicionar membros a uma equipa
        7-  Visualizar projetos atuais
        8-  Visualizar relatórios (projetos e tarefas)
        9-  Enviar relatorios por email
        10- Gerar Dashboard de projetos e tarefas
        11- Sair
       """)


    def processar_selecao(self, selecao):  # definição do menu principal

        if selecao == 1:  # ciclo if para a seleção da opção do menu principal
            print("Criar um projeto")
            projeto = Projeto.adicionar_projeto()
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 2:
            print("Adicionar tarefas a um projeto")
            projeto = Projeto.adicionar_tarefa()
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 3:
            print("Atribuir responsáveis a tarefas")
            tarefa = Tarefa()
            tarefa.atribuir_responsavel()
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 4:
            print("Alterar estado de tarefas")
            tarefa = Tarefa()  # instanciar a classe Tarefa
            tarefa.alterar_status()  # alterar o status da tarefa
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 5:
            print("Consultar estado de tarefas")
            basedados = Basedados()
            basedados.obter_informacoes()
            print(basedados.obter_informacoes())
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 6:
            print("Adicionar membros a uma equipa")
            equipa = Equipa()
            equipa.adicionar_membro()
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 7:
            print("Visualizar projetos atuais")
            basedados = Basedados()
            basedados.informacoes_projeto()
            print(basedados.informacoes_projeto())
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 8:
            print("Visualizar relatórios de projetos e tarefas")
            relatorio = Basedados()
            relatorio.informacoes_projeto()
            relatorio.obter_informacoes()
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 9:
            print("Enviar relatorios de projetos e tarefas por email")
            email = "vfrango@gmail.com"  # ou solicite ao usuário
            senha = "usvr qxid jvdp qtvk"
            projeto = ProjetoEnvio(email, "Projeto de Teste", senha)
            base_dados = "1802925.db"
            projeto.ler_dados(base_dados)
            projeto.enviar_relatorios()
            print("Relatórios enviados com sucesso!")
            wait = input("Pressione qualquer tecla para continuar...")


        elif selecao == 10:
            print("Gerar Dashboard de projetos e tarefas")
            # Cria uma instância da classe Dashboard
            relatorio = Dashboard("1802925.db")
            relatorio.ler_dados()  # Primeiro lê os dados necessários
            relatorio.gerar_dashboard()  # Depois gera o dashboard
            wait = input("Pressione qualquer tecla para continuar...")

        elif selecao == 11:
                print("Sair")
                sys.exit(0)
        else:
                print("Opção inválida, tente novamente!")


#  # polimorfismo para a execução do programa principal
if __name__ == "__main__":
    menu = MenuPrincipal()

    while True:
        menu.exibir_menu()
        try:
            selecao = int(input("Escolha uma opção: "))
            menu.processar_selecao(selecao)
        except ValueError:
            print("Por favor insira uma opção valida!")
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo utilizador. A sair...")
            exit()
