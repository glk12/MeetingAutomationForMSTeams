"""
Módulo para gerenciamento de reuniões do Microsoft Teams usando SQLite.
Fornece operações CRUD (Create, Read, Update, Delete) para reuniões.
"""

import sqlite3

class Reunioes:
    """
    Classe para gerenciar reuniões do Microsoft Teams em banco de dados SQLite.
    
    Attributes:
        nome: Nome identificador da reunião
        horario: Horário da reunião no formato HH:MM
        dia: Dia da semana em inglês (monday, tuesday, etc.)
        senha: Senha da reunião do Teams
        id_reuniao: ID único da reunião do Teams
    """
    def __init__(self, nome=None, horario=None, dia=None, senha=None, id_reuniao=None):
        # Conecta ao banco de dados SQLite
        self.con=sqlite3.connect('reunioes.db')
        self.cur=self.con.cursor()
        # Cria a tabela se não existir
        self.cur.execute("CREATE TABLE IF NOT EXISTS reuniao (nome TEXT, horario TEXT, dia TEXT, id TEXT, senha TEXT)")
        self.con.commit()

        self.nome=nome
        self.dia=dia
        self.horario=horario
        self.senha=senha
        self.id_reuniao=id_reuniao



    def inserir_reuniao(self,nome,horario,dia,id_reuniao,senha):
        """Insere uma nova reunião no banco de dados."""
        self.cur.execute('INSERT INTO reuniao (nome, horario, dia, id_reuniao, senha) VALUES(?,?,?,?,?)',(nome,horario,dia,id_reuniao,senha))
        self.con.commit()

    def deletar_reuniao(self,reuniao):
        """
        Deleta uma reunião do banco de dados.
        Aceita lista, tupla ou string como entrada.
        """
        if isinstance(reuniao, list):
            for r in reuniao:
                self.cur.execute('DELETE FROM reuniao WHERE id_reuniao=?', (r[4],))
        elif isinstance(reuniao, tuple):
            self.cur.execute('DELETE FROM reuniao WHERE id_reuniao=?', (reuniao[4],))
        elif isinstance(reuniao, str):
            self.cur.execute('DELETE FROM reuniao WHERE id_reuniao=?', (reuniao,))
        else:
            return None 

        self.con.commit()
        return True


    def listar_reunioes(self):
        """Retorna todas as reuniões cadastradas no banco de dados."""
        self.cur.execute('SELECT * FROM reuniao')
        reunioes = self.cur.fetchall()
        if len(reunioes) == 0:
            return None
        return reunioes
    
    def editar_reuniao(self,id_reuniao,reuniao):
        """Atualiza os dados de uma reunião existente."""
        self.cur.execute('UPDATE reuniao SET nome=?,horario=?,dia=?,senha=? WHERE id_reuniao=?',(reuniao.nome,reuniao.dia,reuniao.horario,reuniao.senha,id_reuniao))
        self.con.commit()

    def buscar_reuniao_por_id(self, id_reuniao):
        """
        Busca uma reunião pelo ID.
        Retorna uma tupla se encontrar uma reunião, lista se encontrar múltiplas, ou None se não encontrar.
        """
        self.cur.execute('SELECT * FROM reuniao WHERE id_reuniao=?', (id_reuniao,))
        reunioes = self.cur.fetchall()
        if len(reunioes) > 1:
            return reunioes  
        elif len(reunioes) == 1:
            return reunioes[0]  
        else:
            return None   
    
