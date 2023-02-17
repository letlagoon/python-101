from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

#L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
#L1.place(x=30,y=20)

B1 = ttk.Button(GUI,text='เงินมีกี่บาท')
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'ตอนนี้มี้เงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='เงินมีกี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)




GUI.mainloop()
