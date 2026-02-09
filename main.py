"""
Script principal para automação de reuniões do Microsoft Teams.
Executa duas threads: uma para monitorar reuniões e outra para o menu interativo.
"""

import time
from reunioes import Reunioes
import threading
from functions import monitorar_reunioes

# Caminho do executável do Microsoft Teams (ajustar conforme instalação)
path_teams = "C:\\Program Files\\WindowsApps\\MSTeams_25017.203.3370.1174_x64__8wekyb3d8bbwe\\ms-teams.exe"

def menu_usuario():
    """
    Exibe menu interativo para gerenciar reuniões (CRUD).
    Permite inserir, deletar, listar e editar reuniões do banco de dados.
    """
    while True:
        db=Reunioes()
        print('1- Inserir reunião\n2- Deletar reunião\n3- Listar reuniões\n4- Editar reunião')
        num=input('----> ')
        if num=='1':
            # Inserir nova reunião
            nome=input('Nome da reunião: ')
            horario=input('Horário da reunião (HH:MM): ')
            dia=input('Dia da semana da reunião(em inglês): ')
            id=input('ID da reunião: ').strip()
            senha=input('Senha da reunião: ').strip()
            db.inserir_reuniao(nome,horario,dia,id,senha)
        elif num=='2':
            # Deletar reunião existente
            id=input('ID da reunião: ').strip()
            reuniao=db.buscar_reuniao_por_id(id)
            if reuniao is not None:
                if db.deletar_reuniao(reuniao):
                    print('Reunião deletada com sucesso!')
            else:
                print('Reunião não encontrada!')
            time.sleep(1)
        elif num=='3':
            # Listar todas as reuniões
            reunioes=db.listar_reunioes()
            if reunioes is not None:
                for i in reunioes:
                    print(str(i))
            else:
                print('Nenhuma reunião cadastrada!')
            time.sleep(1)
        elif num=='4':
            # Editar reunião existente
            id=input('ID da reunião:').strip()
            reuniao=db.buscar_reuniao_por_id(id)
            if reuniao!= None:
                nome=input('Nome da reunião: ')
                horario=input('Horário da reunião (HH:MM): ')
                dia=input('Dia da semana da reunião(em inglês): ')
                senha=input('Senha da reunião: ').strip()
                nova_reuniao=Reunioes(nome,horario,dia,senha,id)
                db.editar_reuniao(id,nova_reuniao)
                print('Reunião editada com sucesso!')
            else:
                print('Reunião não encontrada!')
            time.sleep(1)
        else:
            print('Comando inválido!')

# Inicia o monitoramento de reuniões
print("Procurando reuniões...")   

# Cria duas threads: uma para monitorar reuniões e outra para o menu do usuário
t1 = threading.Thread(target=monitorar_reunioes)
t2 = threading.Thread(target=menu_usuario)

# Inicia as threads
t1.start()
t2.start()

# Aguarda as threads terminarem (executam indefinidamente)
t1.join()
t2.join()