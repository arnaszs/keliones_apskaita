import PySimpleGUI as sg
from atstumas import skaiciuokle

# Define the layout of the GUI
layout = [
    [sg.Text('Kelionės atstumas (km): '), sg.InputText(key='atstumas')],
    [sg.Text('Kuros sanaudos (l/100km): '), sg.InputText(key='sanaudos')],
    [sg.Text('Kuro bako talpa (l): '), sg.InputText(key='talpa')],
    [sg.Button('Skaiciuoti')],
    [sg.Text(size=(40, 1), key='output')]
    
]

# Create the window and display it
window = sg.Window('Kelionės kalkuliatorius', layout)

# Event loop to process events and get input values
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Skaiciuoti':
        
        print(f"{values}")
        

window.close()
