import tkinter as tk

#point out global total variable
total = 0

#methods for each button press ? 

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

def zero_pressed():
    global total 
    total = int(str(total) + '0')
    message["text"] = total 

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

message = tk.Label(master=root, text=total) #creates message widget
message.grid(row=0,column=0, columnspan=4)

#? NUMBER BUTTON SECTION ?#

#ROW 2
seven = tk.Button(master=root, text='7', command=seven_pressed)
seven.grid(row=2,column=0,sticky="nsew") #remove sticky to stop it from being a big box

eight = tk.Button(master=root, text='8', command=eight_pressed)
eight.grid(row=2,column=1,sticky="nsew")

nine = tk.Button(master=root, text='9', command=nine_pressed)
nine.grid(row=2,column=2,sticky="nsew")

#ROW 3
four = tk.Button(master=root, text='4', command=four_pressed)
four.grid(row=3,column=0,sticky="nsew")

five = tk.Button(master=root, text='5', command=five_pressed)
five.grid(row=3,column=1,sticky="nsew")

six = tk.Button(master=root, text='6', command=six_pressed)
six.grid(row=3,column=2,sticky="nsew")

#ROW 4
one = tk.Button(master=root, text='1', command=one_pressed)
one.grid(row=4,column=0,sticky="nsew")

two = tk.Button(master=root, text='2', command=two_pressed)
two.grid(row=4,column=1,sticky="nsew")

three = tk.Button(master=root, text='3', command=three_pressed)
three.grid(row=4,column=2,sticky="nsew")

#keep the window displaying
root.mainloop()

