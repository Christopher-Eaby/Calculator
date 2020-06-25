# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jun 25 09:17:43 2020
@author: Chris
"""
from tkinter import * #imports everything from GUI module 

#creating a global variable for the expression
expr = ""

#function to clear the input field
def clear(equ):
    #redeclares the global variable for use in the function
    global expr
    expr = ""
    #sets the expression in the input field to tell the user what to do
    equ.set("Please enter an expression.")

#function to perform sums
def summ(num, equ):
    #redeclares the global variable for use in the function
    global expr
    #adds the number to the expression
    expr = expr + str(num)
    #sets the equation to the current expression
    equ.set(expr)
    
def calc(equ):
    #redeclares the global variable for use in the function
    global expr
    #test the expression
    try:
        #evaluates the expression and returns the answer
        result = str(eval(expr))
        #sets the equation to the current expression
        equ.set(result)
    except:
        #resets the expression
        expr = ""
        
def gui():
    #assigns the window to the window manager
    window = Tk()
    #changes the windows title to the specified title
    window.title("GUI Calculator made by Chris")
    #sets the window size
    window.geometry("220x250")
    #assigns string variable type to equation
    equation = StringVar()
    #creates an input field in the window using equation as the placeholder
    input_field = Entry(window, textvariable = equation)
    #sets the height of the input field
    input_field.place(height = 120)
    #creates a grid field for the window, with 4 columns, which have a space 
    #of 50px between
    input_field.grid(columnspan = 4, ipadx = 50, ipady = 30)
    #sets the equation placeholder to the tell the user what to do.
    equation.set("Please enter an expression.")
    
    #creates a button with the number displayed and the colour set to purple
    g1 = Button(window, text = '1', fg = 'white', bg = 'purple'
    #recalls the summ function using a lambda function, which is then added the equation
    , bd = 0, command = lambda: summ(1, equation), height = 2, width = 7)
    #creates a button that is placed in the grid at the specified row and column
    g1.grid(row = 2, column = 0) 
    
    g2 = Button(window, text = '2', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(2, equation), height = 2, width = 7)
    g2.grid(row = 2, column = 1) 
    
    g3 = Button(window, text = '3', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(3, equation), height = 2, width = 7)
    g3.grid(row = 2, column = 2) 
    
    g4 = Button(window, text = '4', fg = 'white', bg = 'purple' 
    , bd = 0, command = lambda: summ(4, equation), height = 2, width = 7)
    g4.grid(row = 3, column = 0) 
    
    g5 = Button(window, text = '5', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(5, equation), height = 2, width = 7)
    g5.grid(row = 3, column = 1) 
    
    g6 = Button(window, text = '6', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(6, equation), height = 2, width = 7)
    g6.grid(row = 3, column = 2) 
    
    g7 = Button(window, text = '7', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(7, equation), height = 2, width = 7)
    g7.grid(row = 4, column = 0) 
    
    g8 = Button(window, text = '8', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(8, equation), height = 2, width = 7)
    g8.grid(row = 4, column = 1) 
    
    g9 = Button(window, text = '9', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(9, equation), height = 2, width = 7)
    g9.grid(row = 4, column = 2) 
    
    g0 = Button(window, text = '0', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ(0, equation), height = 2, width = 7)
    g0.grid(row = 5, column = 0) 
    
    gplus = Button(window, text = '+', fg = 'white', bg = 'purple'
    #recalls the summ function using a lambda function and adds the exponent to the equation
    , bd = 0, command = lambda: summ('+', equation), height = 2, width = 7)
    gplus.grid(row = 2, column = 3) 
    
    gminus = Button(window, text = '-', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ('-', equation), height = 2, width = 7)
    gminus.grid(row = 3, column = 3) 
    
    gmultiply = Button(window, text = '*', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ('*', equation), height = 2, width = 7)
    gmultiply.grid(row = 4, column = 3) 
    
    gdivision = Button(window, text = '/', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: summ('/', equation), height = 2, width = 7)
    gdivision.grid(row = 5, column = 3)
    
    gequal = Button(window, text = '=', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: calc(equation), height = 2, width = 7)
    gequal.grid(row = 5, column = 2) 
    
    gclear = Button(window, text = 'Clear', fg = 'white', bg = 'purple'
    , bd = 0, command = lambda: clear(equation), height = 2, width = 7)
    gclear.grid(row = 5, column = 1) 
    
    #allows for the window and the program to be closed when the 'x' is pressed
    window.mainloop()

#runs the gui
if __name__ == '__main__':
      gui()