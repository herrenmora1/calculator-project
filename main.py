import tkinter as tk

#point out global total variable
total = 0

#methods for each button press ? 
def zero_pressed():
    global total 
    total = int(str(total) + '0')
    message["text"] = total 

def one_pressed():
    global total 
    total = int(str(total) + '1')
    message["text"] = total 

def two_pressed():
    global total 
    total = int(str(total) + '2')
    message["text"] = total 

def three_pressed():
    global total 
    total = int(str(total) + '3')
    message["text"] = total 

def four_pressed():
    global total 
    total = int(str(total) + '4')
    message["text"] = total 

def five_pressed():
    global total 
    total = int(str(total) + '5')
    message["text"] = total 

def six_pressed():
    global total 
    total = int(str(total) + '6')
    message["text"] = total 

def seven_pressed():
    global total 
    total = int(str(total) + '7')
    message["text"] = total 

def eight_pressed():
    global total 
    total = int(str(total) + '8')
    message["text"] = total 
    
def nine_pressed():
    global total 
    total = int(str(total) + '9')
    message["text"] = total 

def clear():
    global total
    total = 0
    message["text"] = total

def backspace():
    global total 
    total = int(total / 10)
    message["text"] = total

def invert():
    global total 
    total = -1 * total 
    message["text"] = total

#^ OPERATION FUNCTIONS HERE ^#
def divide():
    global total
    #TODO

def multiply():
    global total
    #TODO

def subtract():
    global total
    #TODO

def add():
    global total
    #TODO

def equal():
    global total
    #TODO

#^ END OF OPERATION FUNCTIONS HERE ^#

def decimal():
    global total
    #TODO: REALLY HONESTLY NOT SURE WHAT TO DO HERE

root = tk.Tk() #WINDOW
root.title("JACKULATOR REVISED V2")

######! window specifications !######
#window's rows and columns 
root.rowconfigure([0,1,2,3,4,5], minsize=50, weight=1)
root.columnconfigure([0,1,2,3], minsize=50, weight=1)
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
######! end of window specifications !######

#TODO: PUT BUTTON/OPERATION WIDGETS IN HERE

message = tk.Label(master=root, text=total, justify="right", anchor='e') #creates message widget
message.grid(row=0,column=0, columnspan=4)

#? BUTTON SECTION ?#
#ROW 1
invert = tk.Button(master=root, text='+/-', command=invert)
invert.grid(row=1,column=0,sticky="nsew")

backspace = tk.Button(master=root, text='CE', command=backspace)
backspace.grid(row=1,column=1,sticky="nsew")

#TODO: make this work with floats when the decimal comes in 
clear = tk.Button(master=root, text='C', command=clear)
clear.grid(row=1,column=2,sticky="nsew")

divide = tk.Button(master=root, text='/', command=divide)
divide.grid(row=1,column=3,sticky="nsew") 

#ROW 2
seven = tk.Button(master=root, text='7', command=seven_pressed)
seven.grid(row=2,column=0,sticky="nsew") #remove sticky to stop it from being a big box

eight = tk.Button(master=root, text='8', command=eight_pressed)
eight.grid(row=2,column=1,sticky="nsew")

nine = tk.Button(master=root, text='9', command=nine_pressed)
nine.grid(row=2,column=2,sticky="nsew")

multiply = tk.Button(master=root, text='x', command=multiply)
multiply.grid(row=2,column=3,sticky="nsew")

#ROW 3
four = tk.Button(master=root, text='4', command=four_pressed)
four.grid(row=3,column=0,sticky="nsew")

five = tk.Button(master=root, text='5', command=five_pressed)
five.grid(row=3,column=1,sticky="nsew")

six = tk.Button(master=root, text='6', command=six_pressed)
six.grid(row=3,column=2,sticky="nsew")

subtract = tk.Button(master=root, text='-', command=subtract)
subtract.grid(row=3,column=3,sticky="nsew")

#ROW 4
one = tk.Button(master=root, text='1', command=one_pressed)
one.grid(row=4,column=0,sticky="nsew")

two = tk.Button(master=root, text='2', command=two_pressed)
two.grid(row=4,column=1,sticky="nsew")

three = tk.Button(master=root, text='3', command=three_pressed)
three.grid(row=4,column=2,sticky="nsew")

add = tk.Button(master=root, text='+', command=add)
add.grid(row=4,column=3,sticky="nsew")

#ROW 5
zero = tk.Button(master=root, text='0', command=zero_pressed)
zero.grid(row=5, column=0, columnspan=2, sticky="nsew")

decimal = tk.Button(master=root, text='.', command=decimal)
decimal.grid(row=5, column=2, sticky="nsew")

equal = tk.Button(master=root, text="=", command=equal)
equal.grid(row=5, column=3, sticky="nsew")

#keep the window displaying
root.mainloop()

