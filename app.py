import PySimpleGUI as sg
from funkcijos import *
from PIL import Image, ImageTk, ImageSequence

gif_filename = r'img/spinning-awesome.gif'

interframe_duration = Image.open(gif_filename).info['duration']     # get how long to delay between frames
 
# Layout
layout = [
    [sg.Text('Keliones pavadinimas: ', background_color="Dark Cyan"), sg.Input(key='-NAME-')], 
    [sg.Text('Kelionės atstumas (km): ', background_color="Dark Cyan"), sg.Input(key='-DISTANCE-', size=20)],
    [sg.Text('Greitis: ', background_color="Dark Cyan"), sg.Input(key='-SPEED-')],
    [sg.Text('Kuro bako talpa (l): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_CAPACITY-')],
    [sg.Text('Kuro kaina (eur/l): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_PRICE-')],
    [sg.Text('Kuro sanaudos (l/100km): ', background_color="Dark Cyan"), sg.Input(key='-FUEL_CONSUMPTION-')],
    [sg.Checkbox('Maistas', key='-FOOD_CHECK-', background_color="Dark Cyan")],
    [sg.Checkbox('Kelių mokestis', key='-TOLL_CHECK-', background_color="Dark Cyan")],
    [sg.Text('Valiutos tipas: ', background_color="Dark Cyan"), sg.Radio('Eurai', 'RADIO1', key='-EURO_RADIO-', default=True, background_color="Dark Cyan"), sg.Radio('Svarai', 'RADIO1', key='-POUND_RADIO-', background_color="Dark Cyan")],
    [sg.Button('Skaičiuoti', button_color=('white', 'springgreen4'), use_ttk_buttons=True, focus=True), sg.Button('Išvalyti', use_ttk_buttons=True, focus=True), sg.Button('Rodyti ataskaitą', use_ttk_buttons=True, focus=True), sg.Button('Išeiti', button_color=('white', 'firebrick3'), use_ttk_buttons=True, focus=True)],
    [table]
    ]

layout2 = [[sg.Text('Andriaus Kelionės!', background_color='#A37A3B', text_color='#FFF000',  justification='c', key='-T-', font=("Bodoni MT", 40))],
        [sg.Image(key='-IMAGE-')], [sg.Button('Start', size=(15, 2), font=('Helvetica', 14), button_color=('white', 'springgreen4'), pad=(0, 20))] ]    


# Create the window
window = sg.Window('Kelionės kalkuliatorius', layout, 
                size=(1280, 480),
                margins=(None, None), button_color=None, font='Italic 12 bold',
                background_color='Dark Cyan', 
                icon=icon,
                alpha_channel=0.97, use_default_focus=True, grab_anywhere=True, resizable=True,
                element_justification='left', 
                titlebar_font='Italic 12 bold', titlebar_icon=icon)

window2 = sg.Window('Kelionės apskaita', layout2, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)
window2['-T-'].expand(True, True, True)      # Make the Text element expand to take up all available space

CustomMeter()
sudek_el_lst()

for frame in ImageSequence.Iterator(Image.open(gif_filename)):
  event, values = window2.read(timeout=interframe_duration)
  if event == sg.WIN_CLOSED:
    exit(0)
  elif event == 'Start':
    window2.close()
    break
            
  window2['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )

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
            sg.Popup(f"Visos islaidos: {data['total_cost']},\n Visas laikas: {data['travel_time']},\n Kuro sanaudos: {fuel_consumption_total1},\n kuro bako talpa: {data['fuel_capacity']}")
      
    elif event == 'Rodyti ataskaitą':
        pass

    elif event == 'Istrinti kelione':
        pass
              
    elif event == 'Išvalyti':
        for key in ['-NAME-', '-DISTANCE-', '-SPEED-', '-FUEL_CAPACITY-', '-FUEL_PRICE-', '-FUEL_CONSUMPTION-']:
            window[key].update('')
        for key in ['-FOOD_CHECK-', '-TOLL_CHECK-', '-EURO_RADIO-']:
            window[key].update(False)
        window['-EURO_RADIO-'].update(True)

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
                            
        elif event == 'Išvalyti':
            for key in ['-NAME-', '-DISTANCE-', '-SPEED-', '-FUEL_CAPACITY-', '-FUEL_PRICE-', '-FUEL_CONSUMPTION-']:
                window[key].update('')
            window['-FOOD_CHECK-'].update(False)
            window['-TOLL_CHECK-'].update(False)

    # Close the window
    window.close()
