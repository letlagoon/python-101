from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

############CSV##################
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # dalist = ['pen','pencil','eraser']


def readcsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fr = csv.writer(file) #fr = file reader
        data = list(fr)
    return data

#################################

GUI = Tk()
GUI.title('Data Recording Program')
GUI.geometry('500x400')
GUI['bg'] = 'orange'

style = ttk.Style()
style.configure('TButton', background='blue', foreground='blue')

L1 = Label(GUI,text='รายรับรายจ่าย',font=('Angsana New',30),fg='green')
L1.grid(row=0,column=0,columnspan=2)

from datetime import datetime
 
v_data1 = StringVar() # ตัวแปรที่ใช้เก็บข้อความใน GUI
v_data2 = StringVar() # ตัวแปรที่ใช้เก็บข้อความใน GUI
t = datetime.now().strftime('%Y%m%d %H%M%S')
def Button3():
    data = E1.get(),E2.get() # ดึงข้อมูล
    text ='ตอนนี้มีเงินในบัญชี ' + str(int(E1.get()) - int(E2.get())) + ' บาท'
    text1 = [data,text,t]
    writecsv(text1)
    v_data1.set('') #เคลียข้อมูลในช่องกรอก
    v_data2.set('') #เคลียข้อมูลในช่องกรอก
    messagebox.showinfo('เงินในบัญชี',text)

L2 = Label(GUI,text='รายได้: ',font=('Angsana New',15),fg='black')
L2.grid(row=1,column=0,padx=20,pady=20,sticky='W')



E1 = Entry(GUI,textvariable=v_data1)
E1.grid(row=1,column=1,padx=20,pady=20)


L3 = Label(GUI,text='รายจ่าย: ',font=('Angsana New',15),fg='black')
L3.grid(row=2,column=0,padx=20,pady=20,sticky='W')

E2 = Entry(GUI,textvariable=v_data2)
E2.grid(row=2,column=1,padx=20,pady=20)

B3 = ttk.Button(GUI,text='มีเงินเท่าไหร่', style='TButton', command=Button3)
B3.grid(row=4,column=0,padx=20,pady=20,columnspan=2)

GUI.mainloop()
