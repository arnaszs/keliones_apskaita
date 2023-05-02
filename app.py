import PySimpleGUI as sg

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
        try:
            atstumas = float(values['atstumas'])
            sanaudos = float(values['sanaudos'])
            talpa = float(values['talpa'])
            kuro_kaina = 1.5  # Example fuel price
            kaina = (atstumas / 100) * sanaudos * kuro_kaina
            if kaina > 0:
                liko_km = talpa / sanaudos * 100 - atstumas
                if liko_km > 0:
                    output_str = f'Kelionė kainuos {kaina:.2f}€. Liko kuro {liko_km:.1f}km'
                else:
                    output_str = f'Kelionė kainuos {kaina:.2f}€. Kuro neužteks iki paskirties vietos.'
            else:
                output_str = 'Įveskite teisingus skaičius.'
        except ValueError:
            output_str = 'Įveskite teisingus skaičius.'
        window['output'].update(output_str)

window.close()
