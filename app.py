import PySimpleGUI as sg
import json
import os
from funkcijos import *

filename = 'code_data.json'

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
    [sg.Button('Skaičiuoti', use_ttk_buttons=True, focus=True), sg.Button('Išvalyti', use_ttk_buttons=True, focus=True), sg.Button('Rodyti ataskaitą', use_ttk_buttons=True, focus=True), sg.Button('Išeiti', use_ttk_buttons=True, focus=True)]]

# Create the window
window = sg.Window('Kelionės kalkuliatorius', layout, 
                 size=(640, 480),
                 element_padding=None, margins=(None, None), button_color=None, font='Italic 12 bold',
                 background_color='Dark Cyan', border_depth=None,
                 icon=icon,
                 alpha_channel=0.97, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=True, grab_anywhere_using_control=False, keep_on_top=None, resizable=True, 
                 disable_minimize=False, right_click_menu=None, transparent_color=None, debugger_enabled=True,
                 element_justification='left', 
                 titlebar_font='Italic 12 bold', titlebar_icon=icon,
                 scaling=None,
                 metadata=None)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Išeiti'):
        break
    elif event == 'Skaičiuoti':
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

        with open("code_data.json", "r") as f:
            loader = json.load(f)
            with open('code_data.json', 'w') as f:
                loader[keliones_pavadinimas] = data
                json.dump(loader, f, indent=2)

    elif event == 'Rodyti ataskaitą':
        try:
            with open('code_data.json', 'r+', encoding='utf-8') as data:
                data = json.load(data)
        except json.decoder.JSONDecodeError as e:
            print(f'Error reading {filename}: {e}')
            data = {"nepaėja"}
        else:
            sg.Popup(f"{data}")
            data = data


    elif event == 'Išvalyti':
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