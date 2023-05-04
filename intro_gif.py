from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
def gif():
    gif_filename = r'img/spinning-awesome.gif'

    layout = [[sg.Text('Andriaus Kelionės!', background_color='#A37A3B', text_color='#FFF000',  justification='c', key='-T-', font=("Bodoni MT", 40))],
            [sg.Image(key='-IMAGE-')], [sg.Button('Start', size=(15, 2), font=('Helvetica', 14), button_color=('white', 'springgreen4'), pad=(0, 20))] ]

    window = sg.Window('Kelionės apskaita', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)

    window['-T-'].expand(True, True, True)      # Make the Text element expand to take up all available space

    interframe_duration = Image.open(gif_filename).info['duration']     # get how long to delay between frames

    while True:
        for frame in ImageSequence.Iterator(Image.open(gif_filename)):
            event, values = window.read(timeout=interframe_duration)
            if event == sg.WIN_CLOSED:
                exit(0)
            elif event == 'Start':
                window.close()
                break
    

            window['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )


