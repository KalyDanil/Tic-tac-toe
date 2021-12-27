from tkinter import *
clicks=0
def click_button1():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn1.config(text='X',state='disabled')
    else:
        btn1.config(text='O',state='disabled')
def click_button2():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn2.config(text='X',state='disabled')
    else:
        btn2.config(text='O',state='disabled')
def click_button3():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn3.config(text='X',state='disabled')
    else:
        btn3.config(text='O',state='disabled')
def click_button4():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn4.config(text='X',state='disabled')
    else:
        btn4.config(text='O',state='disabled')
def click_button5():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn5.config(text='X',state='disabled')
    else:
        btn5.config(text='O',state='disabled')
def click_button6():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn6.config(text='X',state='disabled')
    else:
        btn6.config(text='O',state='disabled')
def click_button7():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn7.config(text='X',state='disabled')
    else:
        btn7.config(text='O',state='disabled')
def click_button8():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn8.config(text='X',state='disabled')
    else:
        btn8.config(text='O',state='disabled')
def click_button9():
    global clicks
    clicks+=1
    if clicks%2==0:
        btn9.config(text='X',state='disabled')
    else:
        btn9.config(text='O',state='disabled')
def rmk():
    btn1.config(text='',state='normal')
    btn2.config(text='',state='normal')
    btn3.config(text='',state='normal')
    btn4.config(text='',state='normal')
    btn5.config(text='',state='normal')
    btn6.config(text='',state='normal')
    btn7.config(text='',state='normal')
    btn8.config(text='',state='normal')
    btn9.config(text='',state='normal')
root=Tk()
root.title("Крестик/нолики")
root.geometry("150x150+700+350")
btn1=Button(width=3,command=click_button1)
btn1.place(x=5,y=5)
btn2=Button(width=3,command=click_button2)
btn2.place(x=5,y=30)
btn3=Button(width=3,command=click_button3)
btn3.place(x=5,y=55)
btn4=Button(width=3,command=click_button4)
btn4.place(x=35,y=5)
btn5=Button(width=3,command=click_button5)
btn5.place(x=35,y=30)
btn6=Button(width=3,command=click_button6)
btn6.place(x=35,y=55)
btn7=Button(width=3,command=click_button7)
btn7.place(x=65,y=5)
btn8=Button(width=3,command=click_button8)
btn8.place(x=65,y=30)
btn9=Button(width=3,command=click_button9)
btn9.place(x=65,y=55)
remake=Button(text='Начать заново',command=rmk)
remake.place(x=5,y=90)
root.mainloop()

