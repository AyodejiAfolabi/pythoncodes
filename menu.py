def donothing():
    wks=Button(root,text='2')
from tkinter import *
root=Tk()
bigMenu=Menu(root)
menus=Menu(bigMenu)
menus.add_command(label='Open')
menus.add_command(label="New", command=donothing)
root.config(menu=bigMenu)
root.geometry('500x500')
# show=Button(root,text=9999)
# show.pack()
root.mainloop()