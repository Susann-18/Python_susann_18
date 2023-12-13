# from tkinter import *

# def btnClick(number):
#     global val
#     val=val+str(number)
#     data.set(val)

# def btnClear():
#     global val
#     val=""
#     data.set("")

# def btnEquals():
#     global val
#     result=str(eval(val))
#     data.set(result)
# root=Tk()
# root.title("Simple calculator")
# root.geometry('250x300')
# val=""
# data=StringVar()
# display=Entry(root,text=data,bd=29,justify="right",bg="powder blue",font=("Times", "20", "bold italic"))
# display.grid(row=0,columnspan=4)
# btn7=Button(root,text="7",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(7))
# btn7.grid(row=1,column=0)      
# btn8=Button(root,text="8",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8))
# btn8.grid(row=1,column=1)  
# btn9=Button(root,text="9",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9))
# btn9.grid(row=1,column=2) 
# btn_add=Button(root,text="+",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('+'))
# btn_add.grid(row=1,column=3)     
# btn4=Button(root,text="4",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4))
# btn4.grid(row=2,column=0)      
# btn5=Button(root,text="5",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5))
# btn5.grid(row=2,column=1)  
# btn6=Button(root,text="6",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6))
# btn6.grid(row=2,column=2) 
# btn_add=Button(root,text="-",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('-'))
# btn_add.grid(row=2,column=3) 
# btn1=Button(root,text="1",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1))
# btn1.grid(row=3,column=0)      
# btn2=Button(root,text="2",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2))
# btn2.grid(row=3,column=1)  
# btn3=Button(root,text="3",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3))
# btn3.grid(row=3,column=2) 
# btn_add=Button(root,text="*",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
# btn_add.grid(row=3,column=3) 
# btnc=Button(root,text="C",font=("arial",12,"bold"),bd=12,height=2,width=6,command=btnClear)
# btnc.grid(row=4,column=0)      
# btn0=Button(root,text="0",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0))
# btn0.grid(row=4,column=1)  
# btn_div=Button(root,text="/",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('/'))
# btn_div.grid(row=4,column=2) 
# btn_equal=Button(root,text="=",font=("arial",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
# btn_equal.grid(row=4,column=3) 
# root.mainloop()


# from tkinter import *

# ws = Tk()
# ws.title('Calculator')
# ws.geometry('250x400+500+100')
# ws.resizable(0,0)
# num = ''
# def display(number):
#     global num 
#     num = num + str(number)
#     scr_lbl['text'] = num

# def clear_scr():
#     global num
#     num = ''
#     scr_lbl['text'] = num


# def equal_btn():
#      global num
#      add=str(eval(num))
#      scr_lbl['text'] = add
#      num=''
# def equal_btn():
#      global num
#      sub=str(eval(num))
#      scr_lbl['text'] = sub
#      num=''     
# def equal_btn():
#      global num
#      mul=str(eval(num))
#      scr_lbl['text'] = mul
#      num=''
# def equal_btn():
#      global num
#      div=str(eval(num))
#      scr_lbl['text'] = div
#      num=''    

# var = StringVar()


# frame_1 = Frame(ws) 
# frame_1.pack(expand=True, fill=BOTH)

# frame_2 = Frame(ws)
# frame_2.pack(expand=True, fill=BOTH)

# frame_3 = Frame(ws)
# frame_3.pack(expand=True, fill=BOTH)

# frame_4 = Frame(ws)
# frame_4.pack(expand=True, fill=BOTH)


# scr_lbl = Label(
#     frame_1,
#     textvariable='',
#     font=('Arial', 20),
#     anchor = SE,
#     bg = '#595954',
#     fg = 'white' 
#     )
# scr_lbl.pack(expand=True, fill=BOTH)


# key_1 = Button(
#     frame_1,
#     text='1',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(1)
#     )

# key_1.pack(expand=True, fill=BOTH, side=LEFT)

# key_2 = Button(
#     frame_1,
#     text='2',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(2)
#     )

# key_2.pack(expand=True, fill=BOTH, side=LEFT)

# key_3 = Button(
#     frame_1,
#     text='3',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(3)
#     )

# key_3.pack(expand=True, fill=BOTH, side=LEFT)

# key_add = Button(
#     frame_1,
#     text='+',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display('+')
#     )

# key_add.pack(expand=True, fill=BOTH, side=LEFT)

# key_4 = Button(
#     frame_2,
#     text='4',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(4)
#     )

# key_4.pack(expand=True, fill=BOTH, side=LEFT)

# key_5 = Button(
#     frame_2,
#     text='5',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(5)
#     )

# key_5.pack(expand=True, fill=BOTH, side=LEFT)

# key_6 = Button(
#     frame_2,
#     text='6',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(6)
#     )

# key_6.pack(expand=True, fill=BOTH, side=LEFT)

# key_sub = Button(
#     frame_2,
#     text='-',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display('-')
#     )

# key_sub.pack(expand=True, fill=BOTH, side=LEFT)

# key_7 = Button(
#     frame_3,
#     text='7',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(7)
#     )

# key_7.pack(expand=True, fill=BOTH, side=LEFT)

# key_8 = Button(
#     frame_3,
#     text='8',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(8)
#     )

# key_8.pack(expand=True, fill=BOTH, side=LEFT)

# key_9 = Button(
#     frame_3,
#     text='9',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(9)
#     )

# key_9.pack(expand=True, fill=BOTH, side=LEFT)

# key_mul = Button(
#     frame_3,
#     text='*',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display('*')
#     )

# key_mul.pack(expand=True, fill=BOTH, side=LEFT)


# key_clr = Button(
#     frame_4,
#     text='C',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = clear_scr 
#     )

# key_clr.pack(expand=True, fill=BOTH, side=LEFT)

# key_0 = Button(
#     frame_4,
#     text='0',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display(0)
#     )

# key_0.pack(expand=True, fill=BOTH, side=LEFT)

# key_res = Button(
#     frame_4,
#     text='=',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = equal_btn
#     )

# key_res.pack(expand=True, fill=BOTH, side=LEFT)

# key_div = Button(
#     frame_4,
#     text='/',
#     font=('Arial', 22),
#     border = 0,
#     relief = GROOVE,
#     bg = '#2E2E2B',
#     fg = 'white',
#     command = lambda: display('/')
#     )

# key_div.pack(expand=True, fill=BOTH, side=LEFT)

# ws.mainloop()


        