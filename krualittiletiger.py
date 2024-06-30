from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox


##########กำหนดหน้าจอโปรแกรม###########
GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('เมนูร้านครัวแม่เสือสาว') #นี่คือชื่อโปรแกรม
GUI.geometry('500x500') #นี่ืคือขนาดโปรแกรม


#####################ชื่อร้าน############
L1 = Label(GUI, text='เมนูร้านครัวแม่เสือสาว', font=('Angsana New', 30), fg='red')
L1.pack()
L1.place(x=150,y=20)

###################กล่องข้อความราคา################################
def Button1():
    text = 'ราคา'
    messagebox.showinfo(text,'40บาท') 
def Button2():
    text = 'ราคา'
    messagebox.showinfo(text,'55 บาท')
def Button3():
    text = 'ราคา'
    messagebox.showinfo(text,'50บาท')
def Button4():
    text = 'ราคา'
    messagebox.showinfo(text,'20บาท')    
######################################################
FB1 = Frame(GUI)
FB1.place(x=50,y=80)
B1=ttk.Button(FB1,text='ข้าวผัดกะเพรา',command=Button1)
B1.pack(ipadx=20,ipady=20)

FB2 = Frame(GUI)
FB2.place(x=50,y=180)
B2=ttk.Button(FB2,text='แกงจีดเต้าหู้หมูสับ',command=Button2)
B2.pack(ipadx=20,ipady=20)

FB3 = Frame(GUI)
FB3.place(x=50,y=280)
B3=ttk.Button(FB3,text='ผัดมาม่า',command=Button3)
B3.pack(ipadx=20,ipady=20)

FB4 = Frame(GUI)
FB4.place(x=50,y=280)
B4=ttk.Button(FB3,text='โอเลี้ยง ชาไทย ชาเขียว โกโก้',command=Button3)
B4.pack(ipadx=20,ipady=20)


#######################################################

GUI.mainloop()
