def func(data):
    print(data*2)
func(10)
a=3j
b=4j
print(a*b)
numbers=[1,2,3,4,5]
print(sum(numbers))
# Copying a list
fav_foods=['rice','beans','egg']
friend_foods=fav_foods[:]
print('My favourite foods are: ')
print('eba' in friend_foods)
print(f"ffffffffffffffffffffffffffffffffffffffffffffff")
for food in fav_foods:
    print(food)
print('\nwhile my friends also loves:')
for food in friend_foods:
    print(food)
# import math
# print(math.log(math.pi))
# data=7j
# print(data.__pow__(2))

# # data=math.pi

# data=3.141592653589793j
# print (math.log(data))
# data="""Ade is a boy. Boys play soccer but Ade doesn't. Yet Ade enjoys watching soccer"""
# from tkinter import  *
# from tkinter import messagebox
# top=Tk()
# top.geometry("1000x1000")
# q=0
# photo=PhotoImage(file="imagee.png")

# def fun():
#     messagebox.showinfo("Hello Students",x)
#     print(83)
# for x in range(1,20):
#     btn=Button(top, bd=3,text=x,height=2,width=2,font=18,bg="grey",command=fun)
#     q+=20

#     btn.place(x=q+2,y=30)
# bts=Button(image=photo,height=200,width=200)
# bts.place(x=100,y=100)
# c=Canvas(top,bg='red',width=700,height=500)
# place=0,0,400,400
# c.create_arc(place,start=0,extent=150,fill='blue')
# c.create_line(10,10,100,100,fill="yellow")
# checkVal=IntVar()


# Check=Checkbutton(top,text='BUTTON',height=5,width=5,variable=checkVal,onvalue=1,offvalue=0)
# data=StringVar()
# enter=Entry(top,text='Name',textvariable=data)
# enter.pack()
# Check.pack()
# c.place(x=300,y=200)
# # c.pack()
# hs=Button(top,text="FirstName",font='arial')
# hh=Entry(top,width=25)
# hs.pack(side='left')
# hh.pack(side='left')

# top.mainloop()
import os
print(os.getcwd())
os.chdir('..')
print(99)
os.chdir('Python')
print(os.getcwd())


from tkinter import *
from tkinter import messagebox
def mat():
    message=messagebox.showinfo('Hello','Try to learn it')
total=Tk()
box=Frame(total,bg='black',width=300,height=6000)
box.pack()
boxs=Button(box,width=10,height=10,bg='red')
boxs.pack()
imaget=PhotoImage(file='imagee.png')

data=StringVar()
enter=Entry(total,textvariable=data)
data.set(1234)
print(data,'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
enter.pack()
btn=Button(box,image=imaget,width=20,height=20,command=mat)
btn.pack()
# total.geometry('1000x1000')

secFra=Frame(total,bg='green',width=300,height=2000)
secFra.pack()
btn=Button(secFra,text='Ada',bg='yellow',width=10,height=10)
btn.pack()
lab=Label(total,text='The New text')
lab.pack()
mylist=Listbox(total,font=15,bg='red',fg='white')
mylist.insert(1,'Manutd')
mylist.insert(2,'Liverpool')
mylist.insert(2,'Mancity')
# mylist.pack()
total.geometry("200x500")
mymenu=Menubutton(total,text='Davidddddddddddddddd',relief=RAISED)
mymenu.pack()
tvs=Menubutton(total,text='MYMENU',relief=RAISED)
yetvar=IntVar()
datvar=IntVar()
tvs.menu=Menu(tvs,tearoff=0)
tvs['menu']=tvs.menu
tvs.menu.add_checkbutton(label='YES',variable=yetvar)
tvs.menu.add_checkbutton(label="New div",variable=datvar,command=mat)
tvs.pack()
total.mainloop()

# # # from tkinter import *
# # # from tkinter import messagebox
# # top = Tk()
# # top.geometry("100x100")
# # def helloCallBack():
# #     msg=messagebox.showinfo( "Hello Python", "Hello World")
# # B = Button(top, text ="Hello", command = helloCallBack)
# # B.place(x=50,y=50)
# # top.mainloop()p()

