from tkinter import *


expression = ""

def press(num):
	global expression
	expression += str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression=""
	except :
		equation.set("error")
		expression=""

def clear():
	global expression
	expression=""
	equation.set("")


if __name__ == '__main__':
	root = Tk()
	root.title("Calculator")
	root.geometry("430x300")
	equation=StringVar()
	e = Entry(root,textvariable=equation)
	e.grid(columnspan=4,ipadx=70)
	equation.set('enter your expression')

	button1 = Button(root,text="1",padx=40 ,pady=20,command=lambda:press(1))
	button2 = Button(root,text="2",padx=40 ,pady=20,command=lambda:press(2))
	button3 = Button(root,text="3",padx=40 ,pady=20,command=lambda:press(3))
	button4 = Button(root,text="4",padx=40 ,pady=20,command=lambda:press(4))
	button5 = Button(root,text="5",padx=40 ,pady=20,command=lambda:press(5))
	button6 = Button(root,text="6",padx=40 ,pady=20,command=lambda:press(6))
	button7 = Button(root,text="7",padx=40 ,pady=20,command=lambda:press(7))
	button8 = Button(root,text="8",padx=40 ,pady=20,command=lambda:press(8))
	button9 = Button(root,text="9",padx=40 ,pady=20,command=lambda:press(9))
	button0 = Button(root,text="0",padx=40 ,pady=20,command=lambda:press(0))
	button_equal = Button(root,text="=",padx=40 ,pady=20,command=equalpress)
	button_add = Button(root,text="+",padx=40 ,pady=20,command=lambda:press("+"))
	button_sub = Button(root,text="-",padx=40 ,pady=20,command=lambda:press("-"))
	button_pow = Button(root,text="x",padx=40 ,pady=20,command=lambda:press("*"))
	button_div = Button(root,text="/",padx=40 ,pady=20,command=lambda:press("/"))
	button_clear = Button(root,text="CLEAR",padx=40 ,pady=20,command=clear)


	button1.grid(row=3,column=0)
	button2.grid(row=3,column=1)
	button3.grid(row=3,column=2)

	button4.grid(row=2,column=0)
	button5.grid(row=2,column=1)
	button6.grid(row=2,column=2)

	button7.grid(row=1,column=0)
	button8.grid(row=1,column=1)
	button9.grid(row=1,column=2)

	button0.grid(row=4,column=0)
	button_clear.grid(row=4,column=1)
	button_equal.grid(row=4,column=2)
	button_add.grid(row=1,column=3)
	button_sub.grid(row=2,column=3)
	button_pow.grid(row=3,column=3)
	button_div.grid(row=4,column=3)



	root.mainloop()