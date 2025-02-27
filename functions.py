import time
from datetime import datetime as dt
from pywinauto import Application
from reunioes import Reunioes

path_teams = "C:\\Program Files\\WindowsApps\\MSTeams_25017.203.3370.1174_x64__8wekyb3d8bbwe\\ms-teams.exe"

def mute_mic(meeting_window):
    mic= meeting_window.child_window(title='Microfone',control_type="CheckBox")  
    if  mic.is_enabled():
        mic.click_input()

def abrir_reuniao(id_reuniao,senha_reuniao):
    app = Application(backend="uia").start(path_teams)
    time.sleep(2)

    if app.connect(title_re=".*Microsoft Teams.*"):
        print('Teams está conectado!')
    teams_window = app.window(title_re=".*Microsoft Teams.*")

    calendar = teams_window.child_window(title='Calendar', control_type="Button")

    calendar.click_input()

    button=teams_window.child_window(title="Ingressar com uma ID", control_type="Button")
    button.click_input()

    text_boxes = teams_window.descendants(control_type="Edit")
    text_boxes[0].set_text(id_reuniao)
    text_boxes[1].set_text(senha_reuniao)

    button=teams_window.child_window(title="Participar da reunião", control_type="Button")
    button.click_input()
    #Foca na janela da reunião
    meeting_window = app.window(title_re=".*Reunião do Microsoft Teams.*")
    time.sleep(2)
    mute_mic(meeting_window)
    entrar=meeting_window.child_window(title_re='Ingressar*',control_type='Button')  
    entrar.click_input()

def monitorar_reunioes():
    db=Reunioes()
    while True:
        hora=dt.now().strftime("%H:%M")
        reunioes=db.listar_reunioes()
        if len(reunioes)>0:
            for r in reunioes:
                if hora==r[2]:
                    abrir_reuniao(r[4],r[5])
                    print('Reunião iniciada!')
        time.sleep(10) # Verifica a cada 10 segundos
    