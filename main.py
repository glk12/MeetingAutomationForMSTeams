import time
from reunioes import Reunioes
import threading
from functions import monitorar_reunioes

path_teams = "C:\\Program Files\\WindowsApps\\MSTeams_25017.203.3370.1174_x64__8wekyb3d8bbwe\\ms-teams.exe"

def menu_usuario():
    while True:
        db=Reunioes()
        print('1- Inserir reunião\n2- Deletar reunião\n3- Listar reuniões\n4- Editar reunião')
        num=input('----> ')
        if num=='1':
            nome=input('Nome da reunião: ')
            horario=input('Horário da reunião (HH:MM): ')
            dia=input('Dia da semana da reunião(em inglês): ')
            id=input('ID da reunião: ').strip()
            senha=input('Senha da reunião: ').strip()
            db.inserir_reuniao(nome,horario,dia,id,senha)
        elif num=='2':
            id=input('ID da reunião: ').strip()
            reuniao=db.buscar_reuniao_por_id(id)
            if reuniao is not None:
                if db.deletar_reuniao(reuniao):
                    print('Reunião deletada com sucesso!')
            else:
                print('Reunião não encontrada!')
            time.sleep(1)
        elif num=='3':
            reunioes=db.listar_reunioes()
            if reunioes is not None:
                for i in reunioes:
                    print(str(i))
            else:
                print('Nenhuma reunião cadastrada!')
            time.sleep(1)
        elif num=='4':
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


print("Procurando reuniões...")   
t1 = threading.Thread(target=monitorar_reunioes)
t2 = threading.Thread(target=menu_usuario)

t1.start()
t2.start()

t1.join()
t2.join()