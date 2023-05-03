import PySimpleGUI as sg

icon = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAFZklEQVR4nO3TWWxUVRwG8O/uc2fuLHfaKVO6sJRpS9kKCaCCpfKgDSYgEhAe5IFggEBCxKAPJmhifFDiEhMxmAiGKE0KYtkiLpVVC1ikmEKhWKaddtrZp7PfO3fuPT6ZGFMYEHzjez7n/8v3zznA4zxkurq6uLa2NqbYOfpRwz3e2MrBUKjyf4WPXiHT9nUSDwD0EMJvPtBdZhikRWKECcXuUg8CEUKoQ4dAr1lD6XsGiez9dWij79bNpYGRQFJN6rPURLB0xiTW/uRc8aWtm7a232sW+yDwmYEBYd3aKcrO44qn/aNf2hP+voZE2ItEMAJGV8ExLGJSFUIjqYnFZj3Qqt/ZdqTkuc0dTT3nez7PJvQGomlIBOPIp8MwOECnbdBZe2L58qaTxWbdd+Ol6z+rcNU3HxRFqSmvqpjvimCoK4asJCMGAoMRoGo88pSUnTpvaeKRwEveOs1Wy+59DjPVpIe6MTLqRerCEbzIOkBbZ6IDTuS1JAxKRcjvFbZs3y4Um3lfqz7zdrOuZ0ePnv5iGw5+shlnvvkAt/N5vMvkICl9eAIJOCQ7CnoODqfMrlj1Cv9IGgPgqhgy+zotYUF1IyizBSboGE5H4OEkaLoGJ0sjKdpBURTNWMxFf0tR+PUDt596df/ge4oqLG6c1Qw6mUTs0jHIsg01mgICDXYtAX4si4RjBnjRQu6nyT3h9suJuhOXA8f7e286x66cRq1FgdlIob5ERlkmBcFUBo/ZjE5UYYhQoEgBPG8CJwhF8bvCbRdHpwz5BltrZcUp1MgY7HViphBBlMrjiuFEuTgZDsrAgGBBi5HGMakOejYPo6BBfJjGF08dWtDbNzaX0kZRUdeCaj0OcWwAE/NxZLgJqOYUiDSFQC6BOxqPWfQIKiQ3AnYbcrncf4cjkaAjm9FgM7Pw9Q8gMHQDfyh+iI5yeKwaJqgZmDgBQ9IkDCpWeKwWKKwJajZDcwxT9LeMC7cFiXR231cb9Du/g+VYgJhhnToPhG/E9OwohPBVXFSACCVAEjX0spW4UcjBEDTIui3w/Lwp/i1vfvqsPxqpX7R91/43plOpfxvjPvvXdn+/MDR89aKvPwC3W0BlzVxkwsNIKRyun/0O3ddPweysgXtKHWrqaxEZiUJNByCXuCBI5SOBaObl7FDnzplV81vslrJrllmNe8Nq2jJ8Z/jmb+27Tty18fR5jbWVk2V4akMQeAZ1DbPR8ZMXP5/8EVDCaFqxAdcu/IAJNjPWLm9GnzeIwxf8CHIiBN46seCiOkrKajEjEsa1vnNzjArsEfkqRPvPh9ft2NvQ+uGmyLgwC2ZSy7L54HQABChoBO2tZ0HnvJDdpWheuRFBby/cLieqnDyycWD9CwvhqvYgHo1CVTVAEOA7cgxGRsBYyIesqqBcLjgHrhxzAxgf7jj8rUii5eCgwCSaEAoE0XP5FLRcCC67DTPKCRwOG7xDOjq7Y/D7o7h06RwEQQBL5cCyNMwWE4yICloug0mSEYmnUDm5Fn9e7aLuuuquC50h/x0NqWQKgACKqAgH0wZN03Q44Ec66EM8Fk7HYvTw11+2mlLxCKcaToHQdGn1VAk8xUBJ5pHOjMHK0Ih6Y/D130Kp82mSzWaN8UwAQF3dTmv9zMVLRNHaT1ECYVmpw+Va0lg5ccEGm10m8xc9Q0rLyt9fvbqB3717t8XpnGYTgBqapmIACMMwgwJvIqIokbLKaaTEPUkRzWZS4WmMW63Wkru+6r/jcDiWZDKJZQBp1TR0A4As23ckk+lKm832cTwe9/3zvCRJq1RVncPzOGwy2ZYBhljIF3iaxXmG4epy6ZQ/o2ht9zIf53EeOn8BWy1K8ndljBwAAAAASUVORK5CYII='

# Layout
layout = [[sg.Text('Kelionės atstumas (km): ', background_color="Dark Cyan"), sg.Input(key='-DISTANCE-')],
          [sg.Text('Greitis: ', background_color="Dark Cyan"), sg.Input(key='-SPEED-')],
          [sg.Text('Kuro bako talpa (l): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_CAPACITY-')],
          [sg.Text('Kuro kaina (eur/l): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_PRICE-')],
          [sg.Text('Kuro sanaudos (l/100km): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_CONSUMPTION-')],
          [sg.Checkbox('Maistas', key='-FOOD_CHECK-', background_color="Dark Cyan")],
          [sg.Checkbox('Kelių mokestis', key='-TOLL_CHECK-', background_color="Dark Cyan")],
          [sg.Text('Valiutos tipas: ', background_color="Dark Cyan"), sg.Radio('Eurai', 'RADIO1', key='-EURO_RADIO-', default=True, background_color="Dark Cyan"), sg.Radio('Svarai', 'RADIO1', key='-POUND_RADIO-', background_color="Dark Cyan")],
          [sg.Text('Asmeninės išlaidos (eur): ', background_color="Dark Cyan"), sg.Input(key='-PERSONAL_EXPENSES-')],
          [sg.Button('Skaičiuoti', use_ttk_buttons=True, focus=True), sg.Button('Išvalyti', use_ttk_buttons=True, focus=True), sg.Button('Išeiti', use_ttk_buttons=True, focus=True)]]

# Create the window
window = sg.Window('Kelionės kalkuliatorius', layout, default_element_size=None,
                 default_button_element_size=(None, None),
                 auto_size_text=None, auto_size_buttons=None, size=(640, 480),
                 element_padding=None, margins=(None, None), button_color=None, font='Italic 12 bold',
                 background_color='Dark Cyan', border_depth=None,
                 icon=icon,
                 alpha_channel=0.97, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=True, grab_anywhere_using_control=False, keep_on_top=None, resizable=True, 
                 disable_minimize=False, right_click_menu=None, transparent_color=None, debugger_enabled=True,
                 right_click_menu_background_color=None, right_click_menu_text_color=None, right_click_menu_disabled_text_color=None,
                 right_click_menu_selected_colors=(None, None),
                 right_click_menu_font=None, right_click_menu_tearoff=False,
                 finalize=False, element_justification='left', ttk_theme=None, use_ttk_buttons=None, enable_close_attempted_event=False,
                 titlebar_background_color=None, titlebar_text_color=None, titlebar_font='Italic 12 bold', titlebar_icon=icon,
                 scaling=None,
                 metadata=None)

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
    fuel_consumption_total = distance * fuel_consumption / 100
    return f"Fuel consumption: {fuel_consumption_total:.2f} L"

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
    fuel_consumption_total = distance * fuel_consumption / 100
    return f"Fuel consumption: {fuel_consumption_total:.2f} L"

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
        fuel_capacity = values['-FUEL_CAPACITY-']
        fuel_consumption = float(values['-FUEL_CONSUMPTION-'])
        fuel_price = float(values['-FUEL_PRICE-'])
        food_checked = values['-FOOD_CHECK-']
        toll_checked = values['-TOLL_CHECK-']
        euro_checked = values['-EURO_RADIO-']
        pound_checked = values['-POUND_RADIO-']
        total_cost = calculate_total_cost(distance, fuel_consumption, fuel_price, food_checked, toll_checked, euro_checked, pound_checked)
        fuel_consumption_total = fuel_consumption_total(distance, fuel_consumption)
        sg.Popup(f"{total_cost}, {travel_time}, {fuel_consumption_total}, kuro bako talpa: {fuel_capacity}")
    elif event == 'Išvalyti':
        window['-DISTANCE-'].update('')
        window['-FUEL_CONSUMPTION-'].update('')
        window['-FUEL_PRICE-'].update('')
        window['-FUEL_CONSUMPTION_TOTAL-'].update('')
        window['-FOOD_CHECK-'].update(False)
        window['-TOLL_CHECK-'].update(False)
        window['-EURO_RADIO-'].update(True)
        
# Close the window
window.close()

