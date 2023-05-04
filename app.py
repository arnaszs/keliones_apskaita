import PySimpleGUI as sg
from funkcijos import *
from PIL import Image, ImageTk, ImageSequence

sudek_el_lst()
for count in range(100):
    for count, frame in enumerate(ImageSequence.Iterator(Image.open(gif_filename))):
        event, values = window2.read(timeout=interframe_duration)     
        if event == sg.WIN_CLOSED:
            exit(0)
        elif event == 'Išeiti' or event == None:
            exit(0)
        window2['-IMAGE-'].update(data=ImageTk.PhotoImage(frame))
        window2['progress'].update_bar(count +1)
    window2.close()
    break

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

# Close the window
window.close()
