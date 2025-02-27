import sqlite3
class Reunioes:
    def __init__(self, nome=None, horario=None, dia=None, senha=None, id_reuniao=None):
        self.con=sqlite3.connect('reunioes.db')
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS reuniao (nome TEXT, horario TEXT, dia TEXT, id TEXT, senha TEXT)")
        self.con.commit()

        self.nome=nome
        self.dia=dia
        self.horario=horario
        self.senha=senha
        self.id_reuniao=id_reuniao



    def inserir_reuniao(self,nome,horario,dia,id_reuniao,senha):
        self.cur.execute('INSERT INTO reuniao (nome, horario, dia, id_reuniao, senha) VALUES(?,?,?,?,?)',(nome,horario,dia,id_reuniao,senha))
        self.con.commit()

    def deletar_reuniao(self,reuniao):

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
        self.cur.execute('SELECT * FROM reuniao')
        reunioes = self.cur.fetchall()
        if len(reunioes) == 0:
            return None
        return reunioes
    
    def editar_reuniao(self,id_reuniao,reuniao):
        self.cur.execute('UPDATE reuniao SET nome=?,horario=?,dia=?,senha=? WHERE id_reuniao=?',(reuniao.nome,reuniao.dia,reuniao.horario,reuniao.senha,id_reuniao))
        self.con.commit()

    def buscar_reuniao_por_id(self, id_reuniao):
        self.cur.execute('SELECT * FROM reuniao WHERE id_reuniao=?', (id_reuniao,))
        reunioes = self.cur.fetchall()
        if len(reunioes) > 1:
            return reunioes  
        elif len(reunioes) == 1:
            return reunioes[0]  
        else:
            return None   
    
