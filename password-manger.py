import random
#import tkinter as tk
#import tkinter.ttk as ttk
#from tkinter.messagebox import showinfo



#def pswgenerator(self,event):
j = "azertyuiop^qsdf\
	ghjklmù*w<xcvb\
	ABCDEFGHIJKLMNO\
	PQRST{UVWXYZ\
	n,;:!!123456789-\
	/²&éé'()é-_çà)&}[]"
pswlen = 17
password = "".join(random.sample(j,pswlen))
#password.configure(text="your password is : " + str(password))

#def save(self):
#self.password= password 
pwdFor = input("pwd for :")
wb = Workbook()
ws = wb.active
ws['A1'] = "Pwd for"
ws['B1'] = "password"
ws['A2'] = pwdFor
ws['B2'] = password
wb.save(r'C:\Users\zinou\OneDrive\Documents\StupidPasswordGenerator.xlsx')
print("your password is : "+str(password))
#showinfo("Saved","password was saved in cloud")



#def clear(self):
	#entry.delete(0,tk.END)

#win = tk.Tk()
#win.title("Stupid password generator")
#label = tk.Label(win,text="Password for : ")
#label.grid(row=0,column=0)
#entry = tk.Entry(win)
#entry.grid(row=0,column=1,padx=8,pady=8)
#entry.bind("<Return>",pswgenerator)
#buttonSave = ttk.Button(win,text="Save",command=save)
#buttonSave.grid(row=3,column=0)
#buttonClear = ttk.Button(win,text="Clear",command=clear)
#buttonClear.grid(row=3,column=1)
#win.mainloop()