import PySimpleGUI as sg

# Layout
layout = [[sg.Text('Kelionės atstumas (km): '), sg.Input(key='-DISTANCE-')],
          [sg.Text('Greitis: '), sg.Input(key='-SPEED-')],
          [sg.Text('Kuro bako talpa (l): '), sg.Input(key='-TANK_CAPACITY-')],
          [sg.Text('Kuro kaina (eur/l): '), sg.Input(key='-FUEL_PRICE-')],
          [sg.Checkbox('Maistas', key='-FOOD_CHECK-')],
          [sg.Checkbox('Kelių mokestis', key='-TOLL_CHECK-')],
          [sg.Text('Valiutos tipas: '), sg.Radio('Eurai', 'RADIO1', key='-EURO_RADIO-', default=True), sg.Radio('Svarai', 'RADIO1', key='-POUND_RADIO-')],
          [sg.Button('Skaičiuoti'), sg.Button('Išvalyti'), sg.Button('Išeiti')]]

# Create the window
window = sg.Window('Kelionės kalkuliatorius', layout)

def calculate_travel_time(distance, speed):
    time_in_hours = distance / speed
    time_in_minutes = time_in_hours * 60
    return f"Travel time: {time_in_hours:.2f} hours or {time_in_minutes:.2f} minutes"

def calculate_total_cost(distance, speed, tank_capacity, fuel_price, food_checked, toll_checked, euro_checked, pound_checked):
    travel_time = calculate_travel_time(distance, speed)
    fuel_consumption = distance / 100
    fuel_cost = fuel_consumption * fuel_price
    toll_cost = 0
    if toll_checked:
        toll_cost = distance * 0.05
    food_cost = 0
    if food_checked:
        food_cost = 10
    total_cost = fuel_cost + toll_cost + food_cost
    if pound_checked:
        total_cost *= 1.2
    return f"{travel_time}\nTotal cost: {total_cost:.2f}{'£' if pound_checked else '€'}"

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Išeiti'):
        break
    elif event == 'Skaičiuoti':
        # Do the calculations here
        distance = float(values['-DISTANCE-'])
        speed = float(values['-SPEED-'])
        tank_capacity = float(values['-TANK_CAPACITY-'])
        fuel_price = float(values['-FUEL_PRICE-'])
        food_checked = values['-FOOD_CHECK-']
        toll_checked = values['-TOLL_CHECK-']
        euro_checked = values['-EURO_RADIO-']
        pound_checked = values['-POUND_RADIO-']
        total_cost = calculate_total_cost(distance, speed, tank_capacity, fuel_price, food_checked, toll_checked, euro_checked, pound_checked)
        sg.Popup(total_cost)
    elif event == 'Išvalyti':
        window['-DISTANCE-'].update('')
        window['-TANK_CAPACITY-'].update('')
        window['-FUEL_PRICE-'].update('')
        window['-FOOD_CHECK-'].update(False)
        window['-TOLL_CHECK-'].update(False)
        window['-EURO_RADIO-'].update(True)
        
# Close the window
window.close()
