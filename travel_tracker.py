import PySimpleGUI as sg
import json
import os

def calculate_costs(distance, fuel_price, tank_capacity, fuel_consumption, food_budget=0):
    fuel_cost = (distance / 100) * fuel_consumption * fuel_price
    refuels = distance // (tank_capacity * 100)
    if distance % (tank_capacity * 100) != 0:
        refuels += 1
    food_cost = food_budget
    total_cost = fuel_cost * refuels + food_cost
    return total_cost

def save_data(data):
    with open('travel_data.json', 'w') as f:
        json.dump(data, f)

def load_data():
    if os.path.isfile('travel_data.json'):
        with open('travel_data.json', 'r') as f:
            return json.load(f)
    else:
        return {}

def main():
    layout = [
        [sg.Text('How far is the distance to your final destination (km)?*'), sg.InputText(key='distance')],
        [sg.Text('What is the fuel price in the area?*'), sg.InputText(key='fuel_price')],
        [sg.Text('What is your fuel tank capacity?*'), sg.InputText(key='tank_capacity')],
        [sg.Text('What is your fuel consumption?*'), sg.InputText(key='fuel_consumption')],
        [sg.Text('How much money do you prefer to spend on food?(optional)'), sg.InputText(key='food_budget')],
        [sg.Button('Calculate', button_color=('white', 'springgreen4')), sg.Button('Save'), sg.Button('Show'), sg.Button('Total Costs'), sg.Button('Exit', button_color=('white', 'firebrick3'))],
        [sg.Output(size=(80, 20))]
    ]

    window = sg.Window('Europe Travel Tracker', layout)

    data = load_data()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Calculate':
            try:
                distance = float(values['distance'])
                fuel_price = float(values['fuel_price'])
                tank_capacity = float(values['tank_capacity'])
                fuel_consumption = float(values['fuel_consumption'])
                food_budget = float(values['food_budget']) if values['food_budget'] else 0
                total_cost = calculate_costs(distance, fuel_price, tank_capacity, fuel_consumption, food_budget)
                print(f'Total cost of the trip: {total_cost:.2f} euros')
                data['distance'] = distance
                data['fuel_price'] = fuel_price
                data['tank_capacity'] = tank_capacity
                data['fuel_consumption'] = fuel_consumption
                data['food_budget'] = food_budget
                data['total_cost'] = total_cost
            except ValueError:
                print('Please enter valid numbers')
        elif event == 'Save':
            save_data(data)
            print('Data saved successfully')
        elif event == 'Show':
            for key, value in data.items():
                print(f'{key}: {value}')
        elif event == 'Total Costs':
            if 'total_cost' in data:
                print(f'Total cost of the trip: {data["total_cost"]:.2f} euros')
            else:
                print('Please calculate the total cost first')
    
    window.close()

if __name__ == '__main__':
    main()

