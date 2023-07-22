import PySimpleGUI as sg 

total = 0

layout = [[sg.Text(text='0', size=(15,1), key='number')], 
          [sg.Button("⌫"), sg.Button("C"), sg.Button("CE"), sg.Button("/")],
          [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button("x")],
          [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button("-")],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button("+")],
          [sg.Button("+/-"), sg.Button('0'), sg.Button("."), sg.Button("=")]]

#Creates window 
window = sg.Window(title="Calculator", layout=layout, margins=(100, 150))

#event loop 
while True: 
    event, values = window.read()
    #End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    if event == '0' or event == '1' or event == '2' or event == '3' or event == '4' or event == '5' or event == '6' or event == '7' or event == '8' or event == '9':
        total = int(str(total) + sg.Button(event).get_text())
        window['number'].update(total) 
        window.refresh()

window.close()

