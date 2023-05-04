import json
from datetime import date
import PySimpleGUI as sg
from PIL import Image

siandien = date.today().strftime("%d-%m-%Y")
filename = "code_data.json"
icon = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAFZklEQVR4nO3TWWxUVRwG8O/uc2fuLHfaKVO6sJRpS9kKCaCCpfKgDSYgEhAe5IFggEBCxKAPJmhifFDiEhMxmAiGKE0KYtkiLpVVC1ikmEKhWKaddtrZp7PfO3fuPT6ZGFMYEHzjez7n/8v3zznA4zxkurq6uLa2NqbYOfpRwz3e2MrBUKjyf4WPXiHT9nUSDwD0EMJvPtBdZhikRWKECcXuUg8CEUKoQ4dAr1lD6XsGiez9dWij79bNpYGRQFJN6rPURLB0xiTW/uRc8aWtm7a232sW+yDwmYEBYd3aKcrO44qn/aNf2hP+voZE2ItEMAJGV8ExLGJSFUIjqYnFZj3Qqt/ZdqTkuc0dTT3nez7PJvQGomlIBOPIp8MwOECnbdBZe2L58qaTxWbdd+Ol6z+rcNU3HxRFqSmvqpjvimCoK4asJCMGAoMRoGo88pSUnTpvaeKRwEveOs1Wy+59DjPVpIe6MTLqRerCEbzIOkBbZ6IDTuS1JAxKRcjvFbZs3y4Um3lfqz7zdrOuZ0ePnv5iGw5+shlnvvkAt/N5vMvkICl9eAIJOCQ7CnoODqfMrlj1Cv9IGgPgqhgy+zotYUF1IyizBSboGE5H4OEkaLoGJ0sjKdpBURTNWMxFf0tR+PUDt596df/ge4oqLG6c1Qw6mUTs0jHIsg01mgICDXYtAX4si4RjBnjRQu6nyT3h9suJuhOXA8f7e286x66cRq1FgdlIob5ERlkmBcFUBo/ZjE5UYYhQoEgBPG8CJwhF8bvCbRdHpwz5BltrZcUp1MgY7HViphBBlMrjiuFEuTgZDsrAgGBBi5HGMakOejYPo6BBfJjGF08dWtDbNzaX0kZRUdeCaj0OcWwAE/NxZLgJqOYUiDSFQC6BOxqPWfQIKiQ3AnYbcrncf4cjkaAjm9FgM7Pw9Q8gMHQDfyh+iI5yeKwaJqgZmDgBQ9IkDCpWeKwWKKwJajZDcwxT9LeMC7cFiXR231cb9Du/g+VYgJhhnToPhG/E9OwohPBVXFSACCVAEjX0spW4UcjBEDTIui3w/Lwp/i1vfvqsPxqpX7R91/43plOpfxvjPvvXdn+/MDR89aKvPwC3W0BlzVxkwsNIKRyun/0O3ddPweysgXtKHWrqaxEZiUJNByCXuCBI5SOBaObl7FDnzplV81vslrJrllmNe8Nq2jJ8Z/jmb+27Tty18fR5jbWVk2V4akMQeAZ1DbPR8ZMXP5/8EVDCaFqxAdcu/IAJNjPWLm9GnzeIwxf8CHIiBN46seCiOkrKajEjEsa1vnNzjArsEfkqRPvPh9ft2NvQ+uGmyLgwC2ZSy7L54HQABChoBO2tZ0HnvJDdpWheuRFBby/cLieqnDyycWD9CwvhqvYgHo1CVTVAEOA7cgxGRsBYyIesqqBcLjgHrhxzAxgf7jj8rUii5eCgwCSaEAoE0XP5FLRcCC67DTPKCRwOG7xDOjq7Y/D7o7h06RwEQQBL5cCyNMwWE4yICloug0mSEYmnUDm5Fn9e7aLuuuquC50h/x0NqWQKgACKqAgH0wZN03Q44Ec66EM8Fk7HYvTw11+2mlLxCKcaToHQdGn1VAk8xUBJ5pHOjMHK0Ih6Y/D130Kp82mSzWaN8UwAQF3dTmv9zMVLRNHaT1ECYVmpw+Va0lg5ccEGm10m8xc9Q0rLyt9fvbqB3717t8XpnGYTgBqapmIACMMwgwJvIqIokbLKaaTEPUkRzWZS4WmMW63Wkru+6r/jcDiWZDKJZQBp1TR0A4As23ckk+lKm832cTwe9/3zvCRJq1RVncPzOGwy2ZYBhljIF3iaxXmG4epy6ZQ/o2ht9zIf53EeOn8BWy1K8ndljBwAAAAASUVORK5CYII='
gif_filename = r'img/spinning-awesome.gif'
interframe_duration = Image.open(gif_filename).info['duration'] # get how long to delay between frames
lst = []

#create table
table = sg.Table(
    values= lst,
    headings=['Kelionės pavadinimas', "Atstumas", "Greitis", "Kelionės laikas", "Kuro talpa", "Kuro sunaudojimas L/100km", "Kelionės kaina"], 
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', 
    key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True)

# Layout
layout = [
    [sg.Text('Keliones pavadinimas: ', background_color="Dark Cyan"), 
     sg.Input(key='-NAME-')], 
    [sg.Text('Kelionės atstumas (km): ', background_color="Dark Cyan"), 
     sg.Input(key='-DISTANCE-', size=20)],
    [sg.Text('Greitis: ', background_color="Dark Cyan"), 
     sg.Input(key='-SPEED-')],
    [sg.Text('Kuro bako talpa (l): ', background_color="Dark Cyan"), 
     sg.Input(key='-FUEL_CAPACITY-')],
    [sg.Text('Kuro kaina (eur/l): ', background_color="Dark Cyan"), 
     sg.Input(key='-FUEL_PRICE-')],
    [sg.Text('Kuro sanaudos (l/100km): ', background_color="Dark Cyan"), 
     sg.Input(key='-FUEL_CONSUMPTION-')],
    [sg.Checkbox('Maistas', key='-FOOD_CHECK-', background_color="Dark Cyan")],
    [sg.Checkbox('Kelių mokestis', key='-TOLL_CHECK-', background_color="Dark Cyan")],
    [sg.Text('Valiutos tipas: ', background_color="Dark Cyan"), 
     sg.Radio('Eurai', 'RADIO1', key='-EURO_RADIO-', default=True, background_color="Dark Cyan"), 
     sg.Radio('Svarai', 'RADIO1', key='-POUND_RADIO-', background_color="Dark Cyan")],
    [sg.Button('Skaičiuoti', button_color=('white', 'springgreen4'), use_ttk_buttons=True, focus=True), 
     sg.Button('Išvalyti', use_ttk_buttons=True, focus=True), 
     sg.Button('Rodyti ataskaitą', use_ttk_buttons=True, focus=True), 
     sg.Button('Išeiti', button_color=('white', 'firebrick3'), use_ttk_buttons=True, focus=True), 
     sg.Button('Ištrinti', button_color=('white', 'firebrick3'), use_ttk_buttons=True, focus=True)],
    [table]
    ]

layout2 = [[sg.Text('Andriaus kelionės!', background_color='#A37A3B', text_color='#FFF000',  justification='c', key='-T-', font=("Bodoni MT", 40))],
        [sg.Image(key='-IMAGE-')],
        [sg.ProgressBar(interframe_duration, orientation='h', size=(58, 30), key='progress')],
        [sg.Button(button_color=('white', 'firebrick3'), button_text=('Atšaukti'), size=(20, 1), focus=True, key='Išeiti')]]   

# Create the window
window = sg.Window('Kelionės kalkuliatorius', 
                layout, 
                size=(1280, 480),
                margins=(None, None), button_color=None, font='Italic 12 bold',
                background_color='Dark Cyan', 
                icon=icon,
                alpha_channel=0.97, 
                use_default_focus=True, 
                grab_anywhere=True, 
                resizable=True,
                element_justification='left', 
                titlebar_font='Italic 12 bold', titlebar_icon=icon)

window2 = sg.Window('Kelionės apskaita', 
                    layout2, 
                    element_justification='c', 
                    margins=(0,0), 
                    element_padding=(0,0), 
                    finalize=True)

window2['-T-'].expand(True, True, True)  # Make the Text element expand to take up all available space

from typing import Dict, Tuple

# define the types of the input and output data for the function
ValuesDict = Dict[str, str]
TripData = Dict[str, float]

def calculate_trip_info(values: ValuesDict) -> Tuple[TripData, str, float]:
    # extract values from the input dictionary and convert them to appropriate data types
    keliones_pavadinimas = values['-NAME-'] + str(siandien)  # siandien variable is not defined
    distance = float(values['-DISTANCE-'])
    speed = float(values['-SPEED-'])
    fuel_capacity = int(values['-FUEL_CAPACITY-'])  # assuming fuel capacity is an integer value
    fuel_consumption = float(values['-FUEL_CONSUMPTION-'])
    fuel_price = float(values['-FUEL_PRICE-'])
    food_checked = bool(values['-FOOD_CHECK-'])  # assuming food_checked is a boolean value
    toll_checked = bool(values['-TOLL_CHECK-'])  # assuming toll_checked is a boolean value
    euro_checked = bool(values['-EURO_RADIO-'])  # assuming euro_checked is a boolean value
    pound_checked = bool(values['-POUND_RADIO-'])  # assuming pound_checked is a boolean value
    
    # calculate the travel time and total cost of the trip using helper functions
    travel_time = calculate_travel_time(distance, speed)
    total_cost = calculate_total_cost(distance, fuel_consumption, fuel_price, food_checked, toll_checked, euro_checked, pound_checked)
    
    # calculate the total fuel consumption
    fuel_consumption_total1 = fuel_consumption_total(distance, fuel_consumption)
    
    # create a dictionary containing the calculated trip data
    data = {
        "distance": distance,
        "speed": speed,
        "travel_time": travel_time[0],
        "fuel_capacity": fuel_capacity, 
        "fuel_consumption": fuel_consumption,
        "total_cost": total_cost,  
    }
    # return the trip data dictionary, trip name, and total fuel consumption as a tuple
    return data, keliones_pavadinimas, fuel_consumption_total1


def calculate_total_cost(distance: float, fuel_consumption: float, fuel_price: float, food_checked: bool, toll_checked: bool, euro_checked: bool, pound_checked: bool) -> str:
    """
    Calculates the total cost of a trip given the distance, fuel consumption, fuel price, and various expenses.

    Args:
        distance: A float indicating the distance traveled.
        fuel_consumption: A float indicating the fuel consumption rate per 100 km.
        fuel_price: A float indicating the price per liter of fuel.
        food_checked: A bool indicating whether food expenses were incurred.
        toll_checked: A bool indicating whether toll expenses were incurred.
        euro_checked: A bool indicating whether the cost should be in euros (EUR).
        pound_checked: A bool indicating whether the cost should be in pounds (GBP).

    Returns:
        A formatted string indicating the total cost in euros (EUR) or pounds (GBP).
    """
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
    return total_cost

def fuel_consumption_total(distance: float, fuel_consumption: float) -> str:
    """
    Calculates the total fuel consumption given a distance and fuel consumption rate.

    Args:
        distance: A float indicating the distance traveled.
        fuel_consumption: A float indicating the fuel consumption rate per 100 km.

    Returns:
        A formatted string indicating the total fuel consumption in liters.
    """
    fuel_consumption_total = distance * fuel_consumption / 100

    return fuel_consumption_total

def calculate_travel_time(distance: float, speed: float) -> str:
    """
    Calculates the travel time given a distance and speed.

    Args:
        distance: A float indicating the distance traveled.
        speed: A float indicating the speed of travel.

    Returns:
        A formatted string indicating the travel time in hours and minutes.
    """
    time_in_hours = distance / speed
    time_in_minutes = time_in_hours * 60

    return time_in_hours, time_in_minutes

def save_data(keliones_pavadinimas, data):
    with open("code_data.json", "r") as f:
        loader = json.load(f)
        with open('code_data.json', 'w') as f:
            loader[keliones_pavadinimas] = data
            json.dump(loader, f, indent=2)
    return data

def load_data(filename):
    try:
        with open(filename, 'r+', encoding='utf-8') as data:
            data = json.load(data)
    except json.decoder.JSONDecodeError as e:
        print(f'Error reading {filename}: {e}')
        data = {"nepaėja"}
    else:
        return data

def sudek_el_lst():
    file_data = load_data(filename)
    for name, dict in file_data.items():
        row = []
        row.append(name)
        for val in dict.values():
            row.append(val)
        lst.append(row)

def update_table(keliones_pavadinimas, data):
    save_data(keliones_pavadinimas, data)
    old_values = []
    for value in lst:
        old_values.append(value)
    sudek_el_lst()
    for value in lst:
        if value in old_values:
            lst.remove(value)
    return lst

def all_trips():
    file_data = load_data(filename)
    total_expenses = 0
    total_gas = 0
    total_time = 0
    for dict in file_data.values():
        total_expenses += dict['total_cost']
        total_gas += fuel_consumption_total(dict['distance'], dict['fuel_consumption'])
        total_time += calculate_travel_time(dict['distance'], dict['speed'])[0]          
    sg.Popup(f"Visos islaidos: {total_expenses:.2f},\n Visas laikas: {total_time:.2f},\n Kuro sanaudos: {total_gas:.2f},\n")

def remove_data(index):
    file_data = load_data(filename)
    for count, key in enumerate(file_data.keys()):
        if count == index:
            file_data.pop(key)
            lst.pop(index)
            break
    with open(filename, 'w') as f:
        json.dump(file_data, f, indent=2)
    return lst