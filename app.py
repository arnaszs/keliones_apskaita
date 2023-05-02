import PySimpleGUI as sg

# Layout
layout = [[sg.Text('Kelionės atstumas (km): '), sg.Input(key='-DISTANCE-')],
          [sg.Text('Kuro bako talpa (l): '), sg.Input(key='-TANK_CAPACITY-')],
          [sg.Text('Kuro kaina (eur/l): '), sg.Input(key='-FUEL_PRICE-')],
          [sg.Checkbox('Maistas', key='-FOOD_CHECK-')],
          [sg.Checkbox('Kelių mokestis', key='-TOLL_CHECK-')],
          [sg.Text('Valiutos tipas: '), sg.Radio('Eurai', 'RADIO1', key='-EURO_RADIO-', default=True), sg.Radio('Svarai', 'RADIO1', key='-POUND_RADIO-')],
          [sg.Text('Asmeninės išlaidos (eur): '), sg.Input(key='-PERSONAL_EXPENSES-')],
          [sg.Button('Skaičiuoti'), sg.Button('Išvalyti'), sg.Button('Išeiti')]]

# Create the window
window = sg.Window('Kelionės kalkuliatorius', layout)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Išeiti'):
        break
    elif event == 'Skaičiuoti':
        # Do the calculations here
        distance = float(values['-DISTANCE-'])
        tank_capacity = float(values['-TANK_CAPACITY-'])
        fuel_price = float(values['-FUEL_PRICE-'])
        food_checked = values['-FOOD_CHECK-']
        toll_checked = values['-TOLL_CHECK-']
        euro_checked = values['-EURO_RADIO-']
        pound_checked = values['-POUND_RADIO-']
        personal_expenses = float(values['-PERSONAL_EXPENSES-'])
        # TODO: Perform the necessary calculations and display the results
        # You can use the sg.Popup function to display a message box with the results
    elif event == 'Išvalyti':
        window['-DISTANCE-'].update('')
        window['-TANK_CAPACITY-'].update('')
        window['-FUEL_PRICE-'].update('')
        window['-FOOD_CHECK-'].update(False)
        window['-TOLL_CHECK-'].update(False)
        window['-EURO_RADIO-'].update(True)
        window['-PERSONAL_EXPENSES-'].update('')
        
# Close the window
window.close()
