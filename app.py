import PySimpleGUI as sg
from funkcijos import *
import pygame

# initialize pygame mixer
pygame.mixer.init()

# load the sound file
sound = pygame.mixer.Sound('img/morons.MP3')

sudek_el_lst()
gifas()


# play the sound file
sound.play()
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Išeiti'):
        break
        
    elif event == 'Skaičiuoti':
        try:
            data, keliones_pavadinimas, fuel_consumption_total1 = calculate_trip_info(values)
            window['-TABLE-'].update(values=update_table(keliones_pavadinimas, data))
        except Exception as e:
            sg.Popup('Something went wrong', e)
            continue
        else:
            sg.Popup(f"Išlaidos: {data['total_cost']:.2f}, \nLaikas: valandomis {calculate_travel_time(data['distance'], data['speed'])[0]:.2f}, minutemis {calculate_travel_time(data['distance'], data['speed'])[1]:.2f} \nKuro sanaudos: {fuel_consumption_total1:.2f},\nkuro bako talpa: {data['fuel_capacity']}")
      
    elif event == 'Rodyti ataskaitą':
        all_trips()

    elif event == 'Ištrinti':
       data_selected = [row for row in values['-TABLE-']]
       print(data_selected)
       window['-TABLE-'].update(values=remove_data(data_selected[0]))

    elif event == 'Išvalyti':
        for key in ['-NAME-', '-DISTANCE-', '-SPEED-', '-FUEL_CAPACITY-', '-FUEL_PRICE-', '-FUEL_CONSUMPTION-']:
            window[key].update('')
        for key in ['-FOOD_CHECK-', '-TOLL_CHECK-', '-EURO_RADIO-']:
            window[key].update(False)
        window['-EURO_RADIO-'].update(True)


# stop the sound when the program exits
sound.stop()

# Close the window
window.close()