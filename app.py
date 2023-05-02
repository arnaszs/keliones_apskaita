import PySimpleGUI as sg

# Define the PySimpleGUI layout
layout = [
    [sg.Text('Kelionės atstumas (km):'), sg.Input(key='distance')],
    [sg.Text('Kuro bako talpa (l):'), sg.Input(key='tank_size')],
    [sg.Text('Kuro kaina (eur/l):'), sg.Input(key='fuel_cost')],
    [sg.Checkbox('Maistas', key='food')],
    [sg.Checkbox('Kelių mokestis', key='tolls')],
    [sg.Text('Valiutos tipas: Euro')],
    [sg.Text('Asmeninės išlaidos:', size=(20, 1)), sg.Input(key='personal_expenses')],
    [sg.Button('Skaičiuoti'), sg.Button('Išvalyti')],
    [sg.Text('Kelionės pradžios laikas:'), sg.Input(key='start_time')],
    [sg.Multiline(key='history', size=(40, 5))],
    [sg.Text('Kiek laiko truko kiekviena kelionė:'), sg.Multiline(key='duration')],
    [sg.Text('Kiek laiko truko visos kelionės:'), sg.Input(key='total_duration')],
    [sg.Text('Bendra kuro sanaudų suma (eur):'), sg.Input(key='total_fuel_cost')],
]

# Create the PySimpleGUI window
window = sg.Window('Kelionės kalkuliatorius', layout)

# Event loop to process events and get input
while True:
    event, values = window.read()

    # Break out of the loop if the user closes the window or clicks the Exit button
    if event == sg.WINDOW_CLOSED or event == 'Išvalyti':
        break

    # Calculate the total fuel cost based on the input values
    if event == 'Skaičiuoti':
        distance = float(values['distance'])
        tank_size = float(values['tank_size'])
        fuel_cost = float(values['fuel_cost'])
        food = values['food']
        tolls = values['tolls']
        personal_expenses = float(values['personal_expenses'])

        total_fuel_cost = (distance / tank_size) * fuel_cost

        if food:
            total_fuel_cost += 20.0
        if tolls:
            total_fuel_cost += 10.0

        total_fuel_cost += personal_expenses

        # Update the output fields
        window['total_fuel_cost'].update(total_fuel_cost)
        window['history'].update(values['history'] + f'Kelionė: {distance} km, Kaina: {total_fuel_cost} eur\n')
        window['duration'].update(values['duration'] + f'{distance} km: 3 val. 30 min.\n')
        window['total_duration'].update('20 val.')
        
# Close the PySimpleGUI window
window.close()
