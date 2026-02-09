"""
Módulo de funções para automação do Microsoft Teams.
Inclui funções para silenciar microfone, abrir reuniões e monitorar horários agendados.
"""

import time
from datetime import datetime as dt
from pywinauto import Application
from reunioes import Reunioes

# Caminho do executável do Microsoft Teams (ajustar conforme instalação)
path_teams = "C:\\Program Files\\WindowsApps\\MSTeams_25017.203.3370.1174_x64__8wekyb3d8bbwe\\ms-teams.exe"

def mute_mic(meeting_window):
    """
    Silencia o microfone na janela da reunião do Teams.
    
    Args:
        meeting_window: Objeto da janela da reunião do pywinauto
    """
    mic= meeting_window.child_window(title='Microfone',control_type="CheckBox")  
    if  mic.is_enabled():
        mic.click_input()

def abrir_reuniao(id_reuniao,senha_reuniao):
    """
    Abre o Microsoft Teams e entra automaticamente em uma reunião.
    
    Args:
        id_reuniao: ID da reunião do Teams
        senha_reuniao: Senha da reunião (se necessário)
    """
    # Inicia o aplicativo Teams
    app = Application(backend="uia").start(path_teams)
    time.sleep(2)

    # Conecta à janela do Teams
    if app.connect(title_re=".*Microsoft Teams.*"):
        print('Teams está conectado!')
    teams_window = app.window(title_re=".*Microsoft Teams.*")

    # Navega até o calendário
    calendar = teams_window.child_window(title='Calendar', control_type="Button")

    calendar.click_input()

    # Clica em "Ingressar com uma ID"
    button=teams_window.child_window(title="Ingressar com uma ID", control_type="Button")
    button.click_input()

    # Preenche ID e senha da reunião
    text_boxes = teams_window.descendants(control_type="Edit")
    text_boxes[0].set_text(id_reuniao)
    text_boxes[1].set_text(senha_reuniao)

    # Clica em "Participar da reunião"
    button=teams_window.child_window(title="Participar da reunião", control_type="Button")
    button.click_input()
    
    # Foca na janela da reunião e silencia o microfone
    meeting_window = app.window(title_re=".*Reunião do Microsoft Teams.*")
    time.sleep(2)
    mute_mic(meeting_window)
    
    # Clica no botão de ingressar
    entrar=meeting_window.child_window(title_re='Ingressar*',control_type='Button')  
    entrar.click_input()

def monitorar_reunioes():
    """
    Monitora continuamente o banco de dados e abre reuniões no horário agendado.
    Verifica a cada 10 segundos se há reuniões para iniciar.
    """
    db=Reunioes()
    while True:
        hora=dt.now().strftime("%H:%M")
        reunioes=db.listar_reunioes()
        if len(reunioes)>0:
            for r in reunioes:
                if hora==r[2]:
                    abrir_reuniao(r[4],r[5])
                    print('Reunião iniciada!')
        time.sleep(10)  # Verifica a cada 10 segundos
    