import json
from datetime import date
import PySimpleGUI as sg

siandien = date.today().strftime("%d-%m-%Y")
filename = "code_data.json"
icon = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAFZklEQVR4nO3TWWxUVRwG8O/uc2fuLHfaKVO6sJRpS9kKCaCCpfKgDSYgEhAe5IFggEBCxKAPJmhifFDiEhMxmAiGKE0KYtkiLpVVC1ikmEKhWKaddtrZp7PfO3fuPT6ZGFMYEHzjez7n/8v3zznA4zxkurq6uLa2NqbYOfpRwz3e2MrBUKjyf4WPXiHT9nUSDwD0EMJvPtBdZhikRWKECcXuUg8CEUKoQ4dAr1lD6XsGiez9dWij79bNpYGRQFJN6rPURLB0xiTW/uRc8aWtm7a232sW+yDwmYEBYd3aKcrO44qn/aNf2hP+voZE2ItEMAJGV8ExLGJSFUIjqYnFZj3Qqt/ZdqTkuc0dTT3nez7PJvQGomlIBOPIp8MwOECnbdBZe2L58qaTxWbdd+Ol6z+rcNU3HxRFqSmvqpjvimCoK4asJCMGAoMRoGo88pSUnTpvaeKRwEveOs1Wy+59DjPVpIe6MTLqRerCEbzIOkBbZ6IDTuS1JAxKRcjvFbZs3y4Um3lfqz7zdrOuZ0ePnv5iGw5+shlnvvkAt/N5vMvkICl9eAIJOCQ7CnoODqfMrlj1Cv9IGgPgqhgy+zotYUF1IyizBSboGE5H4OEkaLoGJ0sjKdpBURTNWMxFf0tR+PUDt596df/ge4oqLG6c1Qw6mUTs0jHIsg01mgICDXYtAX4si4RjBnjRQu6nyT3h9suJuhOXA8f7e286x66cRq1FgdlIob5ERlkmBcFUBo/ZjE5UYYhQoEgBPG8CJwhF8bvCbRdHpwz5BltrZcUp1MgY7HViphBBlMrjiuFEuTgZDsrAgGBBi5HGMakOejYPo6BBfJjGF08dWtDbNzaX0kZRUdeCaj0OcWwAE/NxZLgJqOYUiDSFQC6BOxqPWfQIKiQ3AnYbcrncf4cjkaAjm9FgM7Pw9Q8gMHQDfyh+iI5yeKwaJqgZmDgBQ9IkDCpWeKwWKKwJajZDcwxT9LeMC7cFiXR231cb9Du/g+VYgJhhnToPhG/E9OwohPBVXFSACCVAEjX0spW4UcjBEDTIui3w/Lwp/i1vfvqsPxqpX7R91/43plOpfxvjPvvXdn+/MDR89aKvPwC3W0BlzVxkwsNIKRyun/0O3ddPweysgXtKHWrqaxEZiUJNByCXuCBI5SOBaObl7FDnzplV81vslrJrllmNe8Nq2jJ8Z/jmb+27Tty18fR5jbWVk2V4akMQeAZ1DbPR8ZMXP5/8EVDCaFqxAdcu/IAJNjPWLm9GnzeIwxf8CHIiBN46seCiOkrKajEjEsa1vnNzjArsEfkqRPvPh9ft2NvQ+uGmyLgwC2ZSy7L54HQABChoBO2tZ0HnvJDdpWheuRFBby/cLieqnDyycWD9CwvhqvYgHo1CVTVAEOA7cgxGRsBYyIesqqBcLjgHrhxzAxgf7jj8rUii5eCgwCSaEAoE0XP5FLRcCC67DTPKCRwOG7xDOjq7Y/D7o7h06RwEQQBL5cCyNMwWE4yICloug0mSEYmnUDm5Fn9e7aLuuuquC50h/x0NqWQKgACKqAgH0wZN03Q44Ec66EM8Fk7HYvTw11+2mlLxCKcaToHQdGn1VAk8xUBJ5pHOjMHK0Ih6Y/D130Kp82mSzWaN8UwAQF3dTmv9zMVLRNHaT1ECYVmpw+Va0lg5ccEGm10m8xc9Q0rLyt9fvbqB3717t8XpnGYTgBqapmIACMMwgwJvIqIokbLKaaTEPUkRzWZS4WmMW63Wkru+6r/jcDiWZDKJZQBp1TR0A4As23ckk+lKm832cTwe9/3zvCRJq1RVncPzOGwy2ZYBhljIF3iaxXmG4epy6ZQ/o2ht9zIf53EeOn8BWy1K8ndljBwAAAAASUVORK5CYII='

lst = []

table = sg.Table(
    values= lst,
    headings=['Keliones pavadinimas', "distance", "speed", "travel time", "fuel capacity", "fuel_comsumption", "total cost"], 
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', 
    key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True)

def calculate_trip_info(values):
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
    
    #all_trip_data = {keliones_pavadinimas, distance, speed, travel_time, fuel_capacity, fuel_consumption, fuel_price, food_checked, toll_checked, euro_checked, pound_checked, total_cost, fuel_consumption_total1}
    data = {
        "distance": distance,
        "speed": speed,
        "travel_time": travel_time,
        "fuel_capacity": fuel_capacity, 
        "fuel_comsumption": fuel_consumption,
        "total_cost": total_cost,
        }
    return data, keliones_pavadinimas, fuel_consumption_total1

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
    fuel_consumption_total = distance * fuel_consumption / 100
    return f"Fuel consumption: {fuel_consumption_total:.2f} L"

def calculate_travel_time(distance, speed):
    time_in_hours = distance / speed
    time_in_minutes = time_in_hours * 60
    return f"Travel time: {time_in_hours:.2f} hours or {time_in_minutes:.2f} minutes"

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

def CustomMeter():
    # layout the form
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(5000, orientation='h',
                              size=(20, 20), key='progress')],
              [sg.Cancel()]]

    # create the form`
    window = sg.Window('Custom Progress Meter', layout)
    progress_bar = window['progress']
    # loop that would normally do something useful
    for i in range(50):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=0, timeout_key='timeout')
        if event == 'Išeiti' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.update_bar(i+1)
    # done with loop... need to destroy the window as it's still open
    window.CloseNonBlocking()

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
          
