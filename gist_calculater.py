from tkinter import *
root=Tk()
root.title('Sk calculater')
root.minsize(width=300,height=300)
root.maxsize(width=300,height=300)
t1=Entry(root,font=("black",22))
t1.grid(row=0,column=0,columnspan=10)
b1=Button(root,text="1", width=5,height=2,fg="blue" ,command=lambda:insertData(1))
b1.grid(row=1,column=1)

b2=Button(root,text="2", width=5,height=2,fg="blue",command=lambda:insertData(2))
b2.grid(row=1,column=2)

b3=Button(root,text="3", width=5,height=2,fg="blue",command=lambda:insertData(3))
b3.grid(row=1,column=3)

b4=Button(root,text="4", width=5,height=2,fg="blue",command=lambda:insertData(4))
b4.grid(row=2,column=1)

b5=Button(root,text="5", width=5,height=2,fg="blue",command=lambda:insertData(5))
b5.grid(row=2,column=2)

b6=Button(root,text="6", width=5,height=2,fg="blue",command=lambda:insertData(6))
b6.grid(row=2,column=3)

b7=Button(root,text="7", width=5,height=2,fg="blue",command=lambda:insertData(7))
b7.grid(row=3,column=1)

b8=Button(root,text="8", width=5,height=2,fg="blue",command=lambda:insertData(8))
b8.grid(row=3,column=2)

b9=Button(root,text="9", width=5,height=2,fg="blue",command=lambda:insertData(9))
b9.grid(row=3,column=3)

b10=Button(root,text="0", width=5,height=2,fg="blue",command=lambda:insertData(0))
b10.grid(row=4,column=2)

def result():
    global find
    r=eval(t1.get())
    t1.delete(0,END)
    t1.insert(END,r)
    find=False

operators=['+','-','*','/','.']
def insertop(op):
    global operators
    if len(t1.get())!=0:
        if t1.get()[-1]==op:
            pass
        elif t1.get()[-1] in operators:
            t1.delete(len(t1.get())-1,END)
            t1.insert(END,op)
        else:
            t1.insert(END, op)
    elif len(t1.get())==0:
        if operators[1]==op:
            t1.insert(END,op)
find=True

def insertData(d):
    global find
    global operators
    if len(t1.get())!=0:
        if t1.get()[-1] in operators:
            t1.insert(END,d)
        elif t1.get()[-1].isdigit:
            if find==False:
                t1.delete(0,END)
                find=True
            t1.insert(END,d)
    elif len(t1.get())==0:
        t1.insert(END,d)

b11=Button(root,text="+", width=5,height=2,fg="blue",command=lambda: insertop('+'))
b11.grid(row=1,column=4)

b12=Button(root,text="-", width=5,height=2,fg="blue",command=lambda: insertop('-'))
b12.grid(row=2,column=4)

b13=Button(root,text="*", width=5,height=2,fg="blue",command=lambda: insertop('*'))
b13.grid(row=3,column=4)

b14=Button(root,text="/", width=5,height=2,fg="blue",command=lambda: insertop('/'))
b14.grid(row=1,column=5)

b15=Button(root,text=")", width=5,height=2,fg="blue",command=lambda: insertop(')'))
b15.grid(row=2,column=5)

def backdata():
    t1.delete(len(t1.get())-1,END)

b16=Button(root,text="X", width=5,height=2,fg="red" ,command=backdata)
b16.grid(row=4,column=4)

def insertdot():
    global operators
    text=t1.get()

    i=0
    for x in range(len(text)-1,-1,-1):
        if text[x] in operators:
            i=x
            break
    if "." in text[i:]:
        pass
    else:
        t1.insert(END,".")
b17=Button(root,text=".", width=5,height=2,fg="blue",command=lambda:insertdot())
b17.grid(row=4,column=3)


b18=Button(root,text="=", width=5,height=2,fg="blue",command=result)
b18.grid(row=4,column=1)

b19=Button(root,text="(", width=5,height=2,fg="blue",command=lambda:insertop('('))
b19.grid(row=3,column=5)

def clearData():
    t1.delete(0,END)

b20=Button(root,text="C", width=5,height=2,fg="red", command=clearData)
b20.grid(row=4,column=5)
root.mainloop()