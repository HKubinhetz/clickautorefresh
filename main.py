# This is Python script that auto reloads pages after a few minutes.

# --------------------------------------- IMPORTS ---------------------------------------
import PySimpleGUI as sg
import time
import pyautogui

# -------------------------------------- VARIABLES  -------------------------------------

flag = False

current_time = 0
start_time = 0

# pos1x = -800
# pos1y = -130
# pos2x = 2000
# pos2y = -130

pos1x = 2000
pos1y = 15
pos2x = 5000
pos2y = 15


def auto_refresh():
    time.sleep(5)

    pyautogui.moveTo(pos1x, pos1y)
    pyautogui.click()
    pyautogui.press('f5')

    time.sleep(1)
    pyautogui.moveTo(pos2x, pos2y)
    pyautogui.click()
    pyautogui.press('f5')

    time.sleep(300)



# ---------------------------------------- LAYOUT ---------------------------------------
sg.theme("GrayGrayGray")
layout = [[sg.Text("Olá! Este é o atualizador automático do CLICK e do DASH! \n"
                   "Desenvolvido por Henrique Kubinhetz em Mar 2022 \n")],
          [sg.Button("Rodar", size=(15, 2)), sg.Button("Parar", size=(15, 2)), sg.Button("Fechar", size=(15, 2))]]

# Create the window
window = sg.Window("CLICK Update", layout)

# Create an event loop
while True:
    event, values = window.read()
    current_time = time.time()

    # End program if user closes window or
    # presses the OK button
    if event == "Fechar" or event == sg.WIN_CLOSED:
        break

    # Starts scanning time!
    elif event == "Rodar":
        start_time = time.time()
        flag = True
        window.perform_long_operation(auto_refresh, '-Operation Done-')

    #  Stops scanning time!
    elif event == "Parar":
        print("Parando!")
        flag = False

    elif event == "-Operation Done-" and flag:
        window.perform_long_operation(auto_refresh, '-Operation Done-')

window.close()