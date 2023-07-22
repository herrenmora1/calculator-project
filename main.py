import PySimpleGUI as sg 
import tkinter as tk

###################################### YEAH PYSIMPLEGUI IS GARBO DOOKIE WATER NAH I AINT TAKING IT BACK ######################################
# total = 0
# layout = [[sg.Text(text='0', size=(15,2), key='number', justification='right')], 
        #   [sg.Button("⌫", size=(2,2)), sg.Button("C", size=(2,2), ), sg.Button("CE", size=(2,2)), sg.Button("/", size=(2,2))],
        #   [sg.Button('7', size=(2,2)), sg.Button('8', size=(2,2)), sg.Button('9', size=(2,2)), sg.Button("x", size=(2,2))],
        #   [sg.Button('4', size=(2,2)), sg.Button('5', size=(2,2)), sg.Button('6', size=(2,2)), sg.Button("-", size=(2,2))],
        #   [sg.Button('1', size=(2,2)), sg.Button('2', size=(2,2)), sg.Button('3', size=(2,2)), sg.Button("+", size=(2,2))],
        #   [sg.Button("+/-", size=(2,2)), sg.Button('0', size=(2,2)), sg.Button(".", size=(2,2)), sg.Button("=", size=(2,2))]]

#creates window 
# window = sg.Window(title="Jackulator", layout=layout, margins=(20, 25), auto_size_text=True, resizable=True, finalize=True)
#minimum size the window can be shrunk to (specific to my pc)
# window.set_min_size((180, 350))

#event loop 
# while True: 
    # event, values = window.read()
    # End program if user closes window
    # if event == sg.WIN_CLOSED:
        # break

    #number input
    # if event == '0' or event == '1' or event == '2' or event == '3' or event == '4' or event == '5' or event == '6' or event == '7' or event == '8' or event == '9':
        # total = int(str(total) + sg.Button(event).get_text())
        # window['number'].update(total) 
    
    #invert the number
    # if event == "+/-":
        # total *= -1
        # window['number'].update(total)

# window.close()

###################################### END OF DOOKIE WATER PYSIMPLEGUI ######################################

root = tk.Tk() #WINDOW
root.title("JACKULATOR REVISED V2")

####### window specifications #######

#window size 
window_width = 360
window_height = 500

#declare minimum window size 
root.minsize(360, 500)

#get screen dimension 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#find center of screen
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#set window to center of screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

####### end of window specifications #######

#TODO: PUT WIDGETS IN HERE
message = tk.Label(root, text="haha made you look") #creates message widget
message.pack() #shows the widget

#keep the window displaying
root.mainloop()

