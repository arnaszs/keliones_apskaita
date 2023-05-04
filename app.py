import PySimpleGUI as sg
import json
import os
from funkcijos import *


lst = ['elementas']
# Layout
layout = [
    [sg.Text('Keliones pavadinimas: ', background_color="Dark Cyan"), sg.Input(key='-NAME-', size=20)], 
    [sg.Text('Kelionės atstumas (km): ', background_color="Dark Cyan"), sg.Input(key='-DISTANCE-', size=20)],
    [sg.Text('Greitis: ', background_color="Dark Cyan"), sg.Input(key='-SPEED-')],
    [sg.Text('Kuro bako talpa (l): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_CAPACITY-')],
    [sg.Text('Kuro kaina (eur/l): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_PRICE-')],
    [sg.Text('Kuro sanaudos (l/100km): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_CONSUMPTION-')],
    [sg.Checkbox('Maistas', key='-FOOD_CHECK-', background_color="Dark Cyan")],
    [sg.Checkbox('Kelių mokestis', key='-TOLL_CHECK-', background_color="Dark Cyan")],
    [sg.Text('Valiutos tipas: ', background_color="Dark Cyan"), sg.Radio('Eurai', 'RADIO1', key='-EURO_RADIO-', default=True, background_color="Dark Cyan"), sg.Radio('Svarai', 'RADIO1', key='-POUND_RADIO-', background_color="Dark Cyan")],
    [sg.Button('Skaičiuoti', button_color=('white', 'springgreen4'), use_ttk_buttons=True, focus=True), sg.Button('Išvalyti', use_ttk_buttons=True, focus=True), sg.Button('Rodyti ataskaitą', use_ttk_buttons=True, focus=True), sg.Button('Išeiti', button_color=('white', 'firebrick3'), use_ttk_buttons=True, focus=True)]
    ]


# Create the window
window = sg.Window('Kelionės kalkuliatorius', layout, 
                 size=(640, 480),
                margins=(None, None), button_color=None, font='Italic 12 bold',
                 background_color='Dark Cyan', 
                 icon=icon,
                 alpha_channel=0.97, use_default_focus=True, grab_anywhere=True, resizable=True,
                 element_justification='left', 
                 titlebar_font='Italic 12 bold', titlebar_icon=icon)
window_table = sg.Window('1')
# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Išeiti'):
        break
    elif event == 'Skaičiuoti':
        try:
        # Do the calculations here
            keliones_pavadinimas = values['-NAME-'] + str(siandien)
            distance = float(values['-DISTANCE-'])
            speed = float(values['-SPEED-'])
            travel_time = calculate_travel_time(distance, speed)
            fuel_capacity = values['-FUEL_CAPACITY-']
            fuel_consumption = float(values['-FUEL_CONSUMPTION-'])
            fuel_price = float(values['-FUEL_PRICE-'])
            food_checked = values['-FOOD_CHECK-']
            toll_checked = values['-TOLL_CHECK-']
            euro_checked = values['-EURO_RADIO-']
            pound_checked = values['-POUND_RADIO-']
            total_cost = calculate_total_cost(distance, fuel_consumption, fuel_price, food_checked, toll_checked, euro_checked, pound_checked)
            fuel_consumption_total1 = fuel_consumption_total(distance, fuel_consumption)
        except Exception as e:
            sg.Popup('Something went wrong', e)
            continue
        else:
            sg.Popup(f"{total_cost}, {travel_time}, {fuel_consumption_total1}, kuro bako talpa: {fuel_capacity}")
        
        data = {
            keliones_pavadinimas: {
                "distance": distance,
                "speed": speed,
                "travel time": travel_time ,
                "fuel capacity": fuel_capacity, 
                "fuel_comsumption": fuel_consumption,
                "total cost": total_cost,
            },
        }
        save_data(keliones_pavadinimas, data)
            
    elif event == 'Rodyti ataskaitą':
        data = load_data(filename)
        sg.Popup(f"{data}")
        for name in data.keys():
            print(name)
                

    elif event == 'Išvalyti':
        window['-NAME-'].update('')
        window['-DISTANCE-'].update('')
        window['-FUEL_CONSUMPTION-'].update('')
        window['-FUEL_CAPACITY-'].update('')
        window['-SPEED-'].update('')
        window['-FUEL_PRICE-'].update('')
        window['-FOOD_CHECK-'].update(False)
        window['-TOLL_CHECK-'].update(False)
        window['-EURO_RADIO-'].update(True)

# Close the window
window.close()

#versija 2