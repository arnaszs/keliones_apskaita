import PySimpleGUI as sg
from funkcijos import *
from funkcijos import calculate_trip_info



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
layout_table = [[table]]



# Create the window
window = sg.Window('Kelionės kalkuliatorius', layout, 
                size=(640, 480),
                margins=(None, None), button_color=None, font='Italic 12 bold',
                background_color='Dark Cyan', 
                icon=icon,
                alpha_channel=0.97, use_default_focus=True, grab_anywhere=True, resizable=True,
                element_justification='left', 
                titlebar_font='Italic 12 bold', titlebar_icon=icon)

window_table = sg.Window('1', layout_table)



CustomMeter()

# Event loop
while True:
    event, values = window.read()
    
    if event in (sg.WINDOW_CLOSED, 'Išeiti'):
        break
        
    elif event == 'Skaičiuoti':
        try:
             trip_info = calculate_trip_info(values)
             keliones_pavadinimas, distance, speed, travel_time, fuel_capacity, fuel_consumption, fuel_price, food_checked, toll_checked, euro_checked, pound_checked, total_cost, fuel_consumption_total1 = trip_info
        except Exception as e:
            sg.Popup('Something went wrong', e)
            continue
        else:
            sg.Popup(f"{total_cost}, {travel_time}, {fuel_consumption_total1}, kuro bako talpa: {fuel_capacity}")
        
        data = {
                "distance": distance,
                "speed": speed,
                "travel time": travel_time,
                "fuel capacity": fuel_capacity, 
                "fuel_comsumption": fuel_consumption,
                "total cost": total_cost,
        }
        save_data(keliones_pavadinimas, data)
            
    elif event == 'Rodyti ataskaitą':
        # sg.Popup(f"{data}")
        sudek_el_lst()

        event = window_table.read()
        if event == sg.WIN_CLOSED:
            window_table.close
            pass
                
    elif event == 'Išvalyti':
        for key in ['-NAME-', '-DISTANCE-', '-SPEED-', '-FUEL_CAPACITY-', '-FUEL_PRICE-', '-FUEL_CONSUMPTION-']:
            window[key].update('')
        for key in ['-FOOD_CHECK-', '-TOLL_CHECK-', '-EURO_RADIO-']:
            window[key].update(False)
        window['-EURO_RADIO-'].update(True)

# Close the window
window.close()

#versija 2