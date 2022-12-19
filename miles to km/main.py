from tkinter import *


window=Tk()
window.config(padx=20,pady=20)
window.title('Miles to KM')

def if_pressed():
    miles=float(inp.get())
    km=round(miles*1.609)
    output.config(text=km)


inp=Entry(width=6)
inp.grid(column=2,row=0)

lable1=Label(text='miles')
lable1.grid(column=3,row=0)

lable2=Label(text='is equal to')
lable2.grid(column=1,row=1)

output=Label(text='0')
output.grid(column=2,row=1)

kms=Label(text='KM')
kms.grid(column=3,row=1)

buton=Button(text='Convert',command=if_pressed)
buton.grid(column=2,row=2)





window.mainloop()