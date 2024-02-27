# basedados.py
import sqlite3


class Basedados:
    def save(self):
        self.conn.commit()

    def check_projeto_existe(self, id_projeto):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_projeto FROM projetos WHERE id_projeto = ?", (id_projeto,))
            row = cursor.fetchone()
            if row is None:
                return False
            else:
                return True

    def __init__(self, basedados_file="1802925.db"):
        self.conn = sqlite3.connect(basedados_file)
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.create_tables()
        self.adicionar_responsavel_column()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS projetos (
                    id_projeto INTEGER PRIMARY KEY,
                    nome TEXT,
                    descricao TEXT,
                    data_inicio TEXT,
                    data_fim_prevista TEXT,
                    status TEXT
                )
            """)

            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tarefas (
                    id_tarefa INTEGER PRIMARY KEY,
                    id_projeto INTEGER,
                    descricao TEXT,
                    data_inicio TEXT,
                    data_fim_prevista TEXT,
                    status TEXT,
                    FOREIGN KEY (id_projeto) REFERENCES projetos (id_projeto)
                        ON DELETE CASCADE
                )
            """)

            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS membros (
                    id_membro INTEGER PRIMARY KEY,
                    id_tarefa INTEGER,
                    membro TEXT,
                    nome TEXT,
                    cargo TEXT,
                    competencias TEXT,
                    tarefas TEXT
                )
            """)

            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS equipa (
                    id_membro INTEGER PRIMARY KEY,
                    id_tarefa INTEGER,
                    nome TEXT,
                    FOREIGN KEY (id_membro) REFERENCES membros (id_membro)
                        ON DELETE CASCADE
                )
            """)

    def adicionar_responsavel_column(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA table_info(tarefas)")
        columns = [info[1] for info in cursor.fetchall()]
        if "responsavel" not in columns:
            self.conn.execute("""
                ALTER TABLE tarefas
                ADD COLUMN responsavel TEXT
            """)
            self.save()

    def adicionar_tarefa(self, tarefa):
        with self.conn:
            self.conn.execute("""
                INSERT INTO tarefas (id_projeto, descricao, data_inicio, data_fim_prevista, status, responsavel)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (tarefa.id_projeto, tarefa.descricao, tarefa.data_inicio, tarefa.data_fim_prevista, tarefa.status, tarefa.responsavel))

    def adicionar_projeto(self, projeto):
        with self.conn:
            self.conn.execute("""
                INSERT INTO projetos (nome, descricao, data_inicio, data_fim_prevista, status)
                VALUES (?, ?, ?, ?, ?)
            """, (projeto.nome, projeto.descricao, projeto.data_inicio, projeto.data_fim_prevista, projeto.status))

    def adicionar_membro(self, membro):
        cursor = self.conn.cursor()

        # Check if the tarefa exists in the tarefas table
        cursor.execute("SELECT * FROM tarefas WHERE id_tarefa = ?", (membro.tarefa,))
        tarefa = cursor.fetchone()

        if tarefa is not None:
            # If the tarefa exists, insert the membro
            self.conn.execute("""
                INSERT INTO membros (tarefa, id_membro, nome, cargo, competencias)
                VALUES (?, ?, ?, ?, ?)
            """, (membro.tarefa, membro.id_membro, membro.nome, membro.cargo, membro.competencias))
            self.conn.commit()
        else:
            print(f"Tarefa {membro.tarefa} does not exist in the tarefas table.")

    def obter_informacoes(self):  # consultar informações
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM tarefas")
            rows = cursor.fetchall()
            for row in rows:
                print(f"ID Tarefa: {row[0]}, ID Projeto: {row[1]}, Status: {row[2]}")
    def informacoes_projeto(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_projeto, nome, data_inicio, data_fim_prevista, status FROM projetos")
            rows = cursor.fetchall()
            for row in rows:
                print(
                    f"ID Projeto: {row[0]}, Nome: {row[1]}, Início: {row[2]}, Previsto Fim: {row[3]}, Status: {row[4]}")

    def enviar_notificacao(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_tarefa, id_projeto, status FROM tarefas")
            rows = cursor.fetchall()
            for row in rows:
                print(f"ID Tarefa: {row[0]}, ID Projeto: {row[1]}, Status: {row[2]}")

    def tarefa_exists(self, id_tarefa):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_tarefa FROM tarefas WHERE id_tarefa = ?", (id_tarefa,))
            row = cursor.fetchone()
            if row is None:
                return False
            else:
                return True

""""

# Ajuste  à BD
conn = sqlite3.connect('1802925.db')

# Create a cursor object
cur = conn.cursor()


cur.execute("DELETE FROM tarefas WHERE id_tarefa = 10")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

"""