# This is Python script that auto reloads pages after a few minutes.

# --------------------------------------- IMPORTS ---------------------------------------
import PySimpleGUI as sg
import time
import pyautogui

# -------------------------------------- VARIABLES  -------------------------------------

flag = False

current_time = 0
start_time = 0
x0, y0 = pyautogui.position()

pos1x = 100
pos1y = 100
update_timer = 300


def auto_refresh():
    time.sleep(3)

    pyautogui.moveTo(pos1x, pos1y)
    pyautogui.click()
    pyautogui.click()
    pyautogui.press('f5')

    time.sleep(update_timer)


def update_coordinates(entradas):
    x1 = int(entradas[0])
    y1 = int(entradas[1])

    return [x1, y1]


# ---------------------------------------- LAYOUT ---------------------------------------
# sg.theme("GrayGrayGray")
sg.theme("SystemDefault")

# TODO - Quantidade dinâmica de campos
# TODO - Tela Configurações
# TODO - File I/O com as coordenadas
# TODO - Modo Clique/Duplo-Clique/Clique F5
# TODO - Timer
layout = [[sg.Text("Olá! Este é o atualizador automático do CLICK e do DASH! \n"
                   "Desenvolvido por Henrique Kubinhetz em Mar 2022 e atualizado \n"
                   "para funcionar em uma tela em em Dez 2023. \n")],
          [sg.Text('Coordenadas - Clique + F5')],
          [sg.Text('Horizonal'), sg.InputText('1000', size=(6, 3)), sg.Text('Vertical'), sg.InputText('1000', size=(6, 3))],
          [sg.Text(f'Coordenada Horizontal: {x0}', key='mousex'), sg.Text(f'Coordenada Vertical: {y0}', key='mousey')],
          [sg.Text('Temporização')],
          [sg.Text('Tempo de Atualização (segundos)'), sg.InputText(f'{update_timer}', size=(6, 3))],
          [sg.Text("")],
          [sg.Button("Rodar", size=(15, 2)), sg.Button("Parar", size=(15, 2)), sg.Button("Fechar", size=(15, 2))]]

# Create the window
window = sg.Window("CLICK Update", layout)

# Create an event loop
while True:
    event, values = window.read(timeout=100)
    current_time = time.time()
    x0, y0 = pyautogui.position()
    window['mousex'].update(f'Coordenada Horizontal: {x0}')
    window['mousey'].update(f'Coordenada Vertical: {y0}')
    window.refresh()

    # End program if user closes window or
    # presses the OK button
    if event == "Fechar" or event == sg.WIN_CLOSED:
        break

    # Starts scanning time!
    elif event == "Rodar":
        start_time = time.time()
        pos1x, pos1y = update_coordinates(values)
        update_timer = int(values[2])
        print(update_timer)
        print("Rodando!")
        flag = True
        window.perform_long_operation(auto_refresh, '-Operation Done-')

    #  Stops scanning time!
    elif event == "Parar":
        print("Parando!")
        flag = False

    elif event == "-Operation Done-" and flag:
        window.perform_long_operation(auto_refresh, '-Operation Done-')

window.close()
