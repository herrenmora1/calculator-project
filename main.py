import tkinter as tk
import math #idk whether i want to use certain math features or not HAHA

#point out global variables
total = 0
temp = 0
lastOperator = '' #options should be /, *, -, +
opFlag = False
decimalFlag = False

#methods for each button press ? 

def checkOpFlag():
    global opFlag
    global total
    global decimalFlag
    
    if opFlag:
       message['text'] = '0'
       opFlag = False 
       decimalFlag = False

def zero_pressed():
    global decimalFlag
    checkOpFlag()
    
    if decimalFlag:
        message['text'] = str(float(message['text'] + '0'))
    else:
        message["text"] = str(int(message['text'] + '0'))

def one_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] + '1'))
    else:
        message['text'] = str(int(message['text'] + '1'))

def two_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] + '2'))
    else:
        message["text"] = str(int(message['text'] + '2'))

def three_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] + '3'))
    else:
        message["text"] = str(int(message['text'] + '3'))

def four_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] + '4'))
    else:
        message["text"] = str(int(message["text"] + '4'))

def five_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] + '5'))
    else:
        message["text"] = str(int(message["text"] + '5'))

def six_pressed():
    global decimalFlag
    checkOpFlag()
    if decimalFlag:
        message['text'] = str(float(message['text'] + '6'))
    else:
        message["text"] = str(int(message["text"] + '6'))

def seven_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] +'7'))
    else:
        message["text"] = str(int(message["text"] + '7'))

def eight_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] + '8'))
    else:
        message["text"] = str(int(message["text"] + '8'))
    
def nine_pressed():
    global decimalFlag
    checkOpFlag()

    if decimalFlag:
        message['text'] = str(float(message['text'] + '9'))
    else:
        message["text"] = str(int(message["text"] + '9'))
    
# NUMBERS END HERE 

#* DECIMALS ARE ANNOYING *#
def decimalEnding():
    if message['text'][-1] == '.':
        return message['text'] + '0'
    else:
        return message['text']

def isInteger(number:float):
    integer = abs(int(number))
    check = abs(number) - integer
    return check == 0

def decimal():
    global total
    global decimalFlag

    checkOpFlag()
    if not decimalFlag:
        message['text'] = str(message['text'] + '.')
        decimalFlag = True
    #TODO: WE GOT THIS CHECK THE STICKY NOTES
#* DECIMALS END HERE *#

def clear():
    global lastOperator
    global total
    global decimalFlag

    clearTemp()

    decimalFlag = False
    lastOperator = ''
    total = 0
    message["text"] = '0'

def backspace():
    global decimalFlag
    clearTemp()
    if len(message['text']) == 1:
        message['text'] = 0
    else:
        message['text'] = message['text'][0:len(message['text'])-1]

    #check if decimal in message['text'] after CE    
    if '.' not in message['text']:
        decimalFlag = False

def invert():
    clearTemp()
    message["text"] = str(int(message['text'])*-1)

def tempCheck():
    global temp 
    global lastOperator

    if temp != 0:
        lastOperator = ''
    clearTemp() 

def clearTemp():
    global temp 
    temp = 0

def repeatOperation():
    global temp 
    global total 
    global lastOperator
    global opFlag

    # if consecutive, temp != 0. if not consecutive, temp != 0. difference is whether opFlag is True or False. 
    # if opFlag is False, total is now message['text'] and temp remains the same. a BUG will happen if operator is immediately clicked before =. 

    if lastOperator == '/':
        if temp == 0: #TODO: DO THIS CHECK FOR EVERY OPERATION HERE
            operation = total / float(decimalEnding()) #assumes that total is an int
            temp = float(decimalEnding()) #^ IMPORTANT FOR REPEATS
        else:
            if not opFlag:
                total = float(decimalEnding())
            operation = total / temp

    elif lastOperator == 'x':
        if temp == 0:
            operation = total * float(decimalEnding())
            temp = float(decimalEnding())
        else:
            if not opFlag:
                total = float(decimalEnding())
            operation = total * temp

    elif lastOperator == '-':
        if temp == 0:
            operation = total - float(decimalEnding())
            temp = float(decimalEnding())
        else:
            if not opFlag:
                total = float(decimalEnding())
            operation = total - temp

    elif lastOperator == '+':
        if temp == 0:
            operation = total + float(decimalEnding())
            temp = float(decimalEnding())
        else:
            if not opFlag:
                total = float(decimalEnding())
            operation = total + temp
    else:
        operation = float(decimalEnding())

    if isInteger(operation):
        operation = int(operation) #set operation to its integer form (without the decimal)

    if temp == 0:
        if lastOperator != '':
            print(str(total) + f"{lastOperator}" + decimalEnding())
        else:
            print(message['text'])
    elif temp != 0:
        if lastOperator != '':
            print(str(total) + f"{lastOperator}" + str(temp))
        else:
            print(message['text'])

    total = operation
    message['text'] = str(total)

def finishOperation():
    global total
    global lastOperator

    if lastOperator == '/':
        operation = total / float(decimalEnding()) #assumes that total is an int
    elif lastOperator == 'x':
        operation = total * float(decimalEnding())
    elif lastOperator == '-':
        operation = total - float(decimalEnding())
    elif lastOperator == '+':
        operation = total + float(decimalEnding())
    else:
        operation = float(decimalEnding())
    
    if isInteger(operation):
        operation = int(operation) #set operation to its integer form (without the decimal)

    if lastOperator != '':
        print(str(total) + f"{lastOperator}" + decimalEnding())
    else:
        print(str(operation))

    total = operation
    message['text'] = str(total) #updates total displayed

#^ OPERATION FUNCTIONS HERE ^#

def divide():
    global total
    global temp
    global lastOperator
    global opFlag
    global decimalFlag

    tempCheck()
    finishOperation() #finishes previous operation

    lastOperator = '/' #sets current operation as division
    opFlag = True #lets calculator know that operation button was JUST pressed, therefore next number click will reset total = 0 
    decimalFlag = False
    print("divide")
    #TODO

def multiply():
    global total
    global temp
    global lastOperator
    global opFlag
    global decimalFlag

    tempCheck()
    finishOperation() #finishes previous operation

    lastOperator = 'x' #sets current operation as division
    opFlag = True #lets calculator know that operation button was JUST pressed, therefore next number click will reset total = 0 
    decimalFlag = False
    print("multiply")
    #TODO

def subtract():
    global total
    global temp
    global lastOperator
    global opFlag
    global decimalFlag

    tempCheck()
    finishOperation() #finishes previous operation

    lastOperator = '-' #sets current operation as division
    opFlag = True #lets calculator know that operation button was JUST pressed, therefore next number click will reset total = 0 
    decimalFlag = False
    print("subtract")
    #TODO

def add():
    global total
    global temp
    global lastOperator
    global opFlag
    global decimalFlag

    tempCheck()
    finishOperation() #finishes previous operation

    lastOperator = '+' #sets current operation as division
    opFlag = True #lets calculator know that operation button was JUST pressed, therefore next number click will reset total = 0 
    decimalFlag = False
    #TODO

def equal():
    global total
    global opFlag
    global lastOperator
    global temp
    global decimalFlag

    repeatOperation()

    opFlag = True 
    decimalFlag = False

#^ END OF OPERATION FUNCTIONS HERE ^#

root = tk.Tk() #WINDOW
root.title("E-JACKULATOR REVISED V2")

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

#THE TOTAL NUMBER THING
message = tk.Label(master=root, text='0', justify="right", anchor='e') #creates message widget
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
#? BUTTON SECTION DONE?#

#keep the window displaying
root.mainloop()

