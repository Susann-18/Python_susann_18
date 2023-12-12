# message box
# from tkinter import *
# from tkinter import messagebox
# root=Tk()
# def callback():
#     m1box=messagebox.askquestion("ANU page","welcome to my this page!",icon="warning")
#     print("your open page")
# btn=Button(root,text="Delete",command=callback)
# btn.place(x=100,y=100)
# root.geometry('500x500')
# root.title("SUJANU")
# root.mainloop()

# list box
# from tkinter import*
# from tkinter import ttk
# root=Tk()
# listbox=Listbox(root,width=45,height=15,selectmode=MULTIPLE)
# listbox.place(x=100,y=200)
# listbox.insert(0,"C")
# listbox.insert(1,"Networking and Hardwaring")
# listbox.insert(2,"Mobile Computing")
# listbox.insert(3,"Java")
# listbox.insert(4,"Python")
# listbox.insert(4,"C++")
# root.geometry('500x500')
# root.title("THIS PAGE IN WELCOME")
# root.mainloop()

# canvas
# from tkinter import*
# root=Tk()
# root.geometry('500x500')
# root.title("HELLO WELCOME")
# canvas=Canvas(root,bg="sky blue",width=150,height=250)
# canvas.place(x=100,y=200)
# rectangle=canvas.create_rectangle(30,20,140,90,fill="light yellow")
# root.mainloop()


# radiobuttion
# from tkinter import *
# root = Tk()
# root.geometry("500x500")
# root.title("Python")
# value1 = StringVar(root, "2")
# rbtn1 = Radiobutton(root, text="Radio Button 1", variable = value1 , value="1")
# rbtn1.place(x=100,y=200)
# rbtn2 = Radiobutton(root, text="Radio Button 2", variable = value1 , value="2")
# rbtn2.place(x=100,y=250)
# rbtn3 = Radiobutton(root, text="Radio Button 3", variable = value1 , value="3")
# rbtn3.place(x=100,y=300)
# mainloop()

# frame
# from tkinter import *
# root = Tk()
# root.geometry("300x150")
# label = Label(root, text ='Python', font = "60")
# label.place(x=100,y=100)
# botm1 = Frame(root, bg="green", width=120, height=100)
# botm1.place(x=100,y=150)
# top1 = Frame(root, bg="red", width=120, height=100)
# top1.place(x=500,y=250)
# root.mainloop()

# paned window
# from tkinter import*
# from tkinter import ttk
# root=Tk()
# root.geometry('400x400')
# root.title("Python")
# pw=ttk.PanedWindow(root,orient=HORIZONTAL)
# pw.place(x=100,y=100)
# frame1=ttk.Frame(pw,relief=SUNKEN)
# frame2=ttk.Frame(pw,relief=SUNKEN)
# pw.add(frame1,weight=1)
# pw.add(frame2,weight=3)
# root.mainloop()


# from tkinter import *
# from tkinter import ttk

# root = Tk()
# #Paned Window
# pw = ttk.PanedWindow(root, orient=HORIZONTAL)
# pw.pack(fill=BOTH, expand=True)
# frame1 = ttk.Frame(pw, relief=SUNKEN)
# frame2 = ttk.Frame(pw, relief=SUNKEN)
# pw.add(frame1, weight=1)
# pw.add(frame2,weight=3)

# root.geometry("400x240")
# root.title("PythonLobby.com")
# root.mainloop()