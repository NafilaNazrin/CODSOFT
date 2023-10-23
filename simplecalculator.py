from tkinter import*
eqntext=""
def btn_click(num):
    global eqntext
    
    eqntext += str(num)
    
    num_disp.set(eqntext)
    
def btn_equalto():
    global eqntext
    try:
        equate= str(eval(eqntext))

        num_disp.set(equate)

        eqntext = equate

    except SyntaxError:
        num_disp.set("Syntax Error")

        eqntext = ""

    except ZeroDivisionError:
        num_disp.set("Error")

        eqntext = "" 
    
def btn_clearall():
    global eqntext

    num_disp.set("")

    eqntext=""
#------------------------------
root = Tk()
root.title("Calculator")
root.geometry("600x800")


num_disp = StringVar()

label= Label(root, textvariable = num_disp, font=('helvetica', 20),
             bg='white', width=30, height=2)
label.pack()

frame = Frame(root)
frame.pack()
#------------------------------

btn1 = Button(frame, text='1', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(1))
btn1.grid(row=0, column=0)

btn2 = Button(frame, text='2', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(2))
btn2.grid(row=0, column=1)

btn3 = Button(frame, text='3', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(3))
btn3.grid(row=0, column=2)

plus = Button(frame, text='+', width=10, height=5,font=40, fg='yellow', bg='navy',
              command = lambda: btn_click('+'))
plus.grid(row=0, column=3)

btn4 = Button(frame, text='4', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(4))
btn4.grid(row=1, column=0)

btn5 = Button(frame, text='5', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(5))
btn5.grid(row=1, column=1)

btn6 = Button(frame, text='6', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(6))
btn6.grid(row=1, column=2)

minus = Button(frame, text='-', width=10, height=5,font=40, fg='yellow', bg='navy',
              command = lambda: btn_click('-'))
minus.grid(row=1, column=3)

btn7 = Button(frame, text='7', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(7))
btn7.grid(row=2, column=0)

btn8 = Button(frame, text='8', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(8))
btn8.grid(row=2, column=1)

btn9 = Button(frame, text='9', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(9))
btn9.grid(row=2, column=2)

multiple = Button(frame, text='*', width=10, height=5,font=40, fg='yellow', bg='navy',
              command = lambda: btn_click('*'))
multiple.grid(row=2, column=3)

percent = Button(frame, text='%', width=10, height=5,font=40, fg='yellow', bg='navy',
              command = lambda: btn_click('%'))
percent.grid(row=3, column=0)

btn0 = Button(frame, text='0', width=10, height=5,font=40, fg='white', bg='red',
              command = lambda: btn_click(0))
btn0.grid(row=3, column=1)

deci = Button(frame, text='.', width=10, height=5,font=40, fg='yellow', bg='navy',
              command = lambda: btn_click('.'))
deci.grid(row=3, column=2)

divide = Button(frame, text='/', width=10, height=5,font=40, fg='yellow', bg='navy',
              command = lambda: btn_click('/'))
divide.grid(row=3, column=3)

clear = Button(frame, text='Clear', width=31, height=5,font=40, fg='yellow', bg='navy',
              command = btn_clearall)
clear.grid(row=4, column=0, columnspan=3)

equal = Button(frame, text='=', width=10, height=5,font=40, fg='yellow', bg='navy',
              command = btn_equalto)
equal.grid(row=4, column=3)


root.mainloop()
