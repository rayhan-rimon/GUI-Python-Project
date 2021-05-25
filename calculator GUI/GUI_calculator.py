from tkinter import *  #Import tkinter all function *

window = Tk()

window.title('Calculator') # This is desktop apps title
window.geometry('355x475') # calculator width & height
window.resizable(False, False) # Window width & height resize off
window.config(bg='#A9A9A9') # Calculator BG color
window.iconbitmap('icon.ico') # Change icon

# Main program start...
expression = ''
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression

    try:
        total = str(eval(expression))

        equation.set(total)
        expression =''
    except:
        equation.set('error')
        expression = ''

def clearpress():
    global expression

    expression = ''
    equation.set('0')



button_frame = Frame(window, bg='#A9A9A9')
button_frame.pack()

equation = StringVar()
equation.set('0')
# Main Program end

# Calculator button Style Start...
expression_field = Entry(button_frame, textvariable=equation, justify='right', font=('arial', 20, 'bold'))


button1 = Button(button_frame, text='1',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(1))
button2 = Button(button_frame, text='2',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(2))
button3 = Button(button_frame, text='3',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(3))
addition = Button(button_frame, text='+',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press('+'))

button4 = Button(button_frame, text='4',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(4))
button5 = Button(button_frame, text='5',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(5))
button6 = Button(button_frame, text='6',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(6))
subtract = Button(button_frame, text='-',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press('-'))

button7 = Button(button_frame, text='7',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(7))
button8 = Button(button_frame, text='8',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(8))
button9 = Button(button_frame, text='9',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(9))
multiply = Button(button_frame, text='*',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press('*'))

button0 = Button(button_frame, text='0',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press(0))
decimal = Button(button_frame, text='.',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press('.'))
clear = Button(button_frame, text='c',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command = clearpress)
division = Button(button_frame, text='/',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=8, height=3, command=lambda:press('/'))

equal = Button(button_frame, text='=',font=('time new roman',12), relief='ridge', bd=1, bg='#A9A9A9', width=35, height=3, command=equalpress)
# Calculator Button style end..

# 0 row mean 1st line  Display Position on this screen
expression_field.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=25, pady=15) #display position

# 1st row mean 2nd line Button Position on this screen
button1.grid(row=1, column=0) 
button2.grid(row=1, column=1)  
button3.grid(row=1, column=2)  
addition.grid(row=1, column=3)  

# 2nd row mean 3rd line  Button Position on this screen
button4.grid(row=2, column=0)  
button5.grid(row=2, column=1)  
button6.grid(row=2, column=2)  
subtract.grid(row=2, column=3)  

# 3rd row mean 4th line  Button Position on this screen
button7.grid(row=3, column=0)  
button8.grid(row=3, column=1)  
button9.grid(row=3, column=2) 
multiply.grid(row=3, column=3) 

# 4th row mean 5th line  Button Position on this screen
button0.grid(row=4, column=0) 
decimal.grid(row=4, column=1) 
clear.grid(row=4, column=2) 
division.grid(row=4, column=3) 

# 5th row mean 6th line  Button Position on this screen
equal.grid(row=5, column=0, columnspan=4)


window.mainloop()


