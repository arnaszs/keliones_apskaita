import PySimpleGUI as sg

# Layout
layout = [[sg.Text('Kelionės atstumas (km): '), sg.Input(key='-DISTANCE-')],
          [sg.Text('Greitis: '), sg.Input(key='-SPEED-')],
          [sg.Text('Kuro sanaudos: '), sg.Input(key='-FUEL_CONSUMPTION-')],
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

def calculate_total_cost(distance, fuel_consumption, fuel_price, food_checked, toll_checked, euro_checked, pound_checked):
    fuel_cost = distance * fuel_consumption * fuel_price / 100
    food_cost = 0
    toll_cost = 0
    if food_checked:
        food_cost = 10 # TODO: calculate actual food cost
    if toll_checked:
        toll_cost = 5 # TODO: calculate actual toll cost
    euro_to_pound_rate = 0.8 # TODO: replace with actual exchange rate
    if pound_checked:
        fuel_cost *= euro_to_pound_rate
        food_cost *= euro_to_pound_rate
        toll_cost *= euro_to_pound_rate
    total_cost = fuel_cost + food_cost + toll_cost
    currency = 'EUR' if euro_checked else 'GBP'
    return f"Total cost: {total_cost:.2f} {currency}"

def fuel_consumption_total(distance, fuel_consumption):
    fuel_consumption_totall = (distance / 100) * fuel_consumption
    return str(fuel_consumption_totall)




# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Išeiti'):
        break
    elif event == 'Skaičiuoti':
        # Do the calculations here
        distance = float(values['-DISTANCE-'])
        speed = float(values['-SPEED-'])
        travel_time = calculate_travel_time(distance, speed)
        # sg.Popup(travel_time) # <-- gauname kelionės laiką
        fuel_consumption = float(values['-FUEL_CONSUMPTION-'])
        fuel_price = float(values['-FUEL_PRICE-'])
        food_checked = values['-FOOD_CHECK-']
        toll_checked = values['-TOLL_CHECK-']
        euro_checked = values['-EURO_RADIO-']
        pound_checked = values['-POUND_RADIO-']
        total_cost = calculate_total_cost(distance, fuel_consumption, fuel_price, food_checked, toll_checked, euro_checked, pound_checked)
        sg.Popup(total_cost, travel_time, fuel_consumption_total) # <-- gauname kelionės išlaidas
    elif event == 'Išvalyti':
        window['-DISTANCE-'].update('')
        window['-FUEL_CONSUMPTION-'].update('')
        window['-FUEL_PRICE-'].update('')
        window['-FOOD_CHECK-'].update(False)
        window['-TOLL_CHECK-'].update(False)
        window['-EURO_RADIO-'].update(True)
        
# Close the window
window.close()

