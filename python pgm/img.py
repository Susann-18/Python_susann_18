# from tkinter import *
# from tkinter import ttk
# root = Tk()
# label = Label(root, text="This is Image")
# label.place(side=TOP, pady=10)
# path = PhotoImage(file="C:/Users/Cyber Security/Pictures/bird.jpg")
# label_image = Label(root, image=path, width=400, height=400)
# label_image.place()
# root.geometry("600x440")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# label = Label(root, text="This is Image")
# label.place(x=50,y=100)
# image = Image.open("C:/Users/Cyber Security/Pictures/flower.jpg")
# tk_image = ImageTk.PhotoImage(image)
# label_image = Label(root, image=tk_image, width=400, height=400)
# label_image.place(x=100,y=200)
# root.geometry("600x440")
# root.title("myflower")
# root.mainloop()

# from tkinter import*
# from PIL import Image,ImageTk
# root=Tk()
# lb=Label(root,text="Image")
# lb.place(x=600,y=90)
# root.configure(bg="sky blue")
# image=Image.open("C:/Users/Cyber Security/Pictures/sunset.jpg")
# tk_image = ImageTk.PhotoImage(image)
# label_image = Label(root, image=tk_image,)
# label_image.place(x=300,y=200)
# root.geometry("600x440")
# root.title("myflower")
# root.mainloop()

# from tkinter import *
# def login():
#     entered_username = username_entry.get()
#     entered_password = password_entry.get()
# #     # Check if the entered username and password match predefined values
#     if entered_username == "admin" and entered_password == "password":
#         result_label.config(text="Login successful!", fg="green")
#     else:
#         result_label.config(text="Login failed. Please try again.", fg="red")
# root = Tk()
# root.title("Customized Login Page")
# root.geometry("300x200")
# root.config(bg="#8d1772")
# username_label = Label(root, text="Username:",bg="#e6caf9")
# username_label.pack(pady=5)
# username_entry = Entry(root)
# username_entry.pack(pady=5)
# password_label = Label(root, text="Password:")
# password_label.pack(pady=5)
# password_entry = Entry(root, show="*")  # Show '*' for password entry
# password_entry.pack(pady=5)
# login_button = Button(root, text="Login", command=login)
# login_button.pack(pady=10)
# result_label = Label(root, text="",bg="#e6caf9")
# result_label.pack()
# root.mainloop()


# from tkinter import *
# from PIL import Image,ImageTk
# root=Tk()
# root.title("WEBSITE")
# root.geometry('1000x1000')
# root.config(bg="light yellow")
# image=Image.open("C:/Users/Cyber Security/Pictures/christmas.jpg")
# tk_image = ImageTk.PhotoImage(image)
# label_image = Label(root, image=tk_image, width=500, height=500)
# label_image.place(x=100,y=500)
# def clicked():
#     print("I am clicked")
# lb1 = Label(root, text="christmas", font=("", 40), bg="light yellow", fg="red")
# lb1.place(x=500, y=50) 
# lb2 = Label(root, text="Username", font=("Times", "20", "bold italic"), fg="dark blue",bg="light yellow")
# lb2.place(x=25, y=200)
# entry1 = Entry(root)
# entry1.place(x=200, y=215)
# lb3 = Label(root, text="Password", font=("Times", "20", "bold italic"), fg="dark blue",bg="light yellow")
# lb3.place(x=25, y=300)
# entry2 = Entry(root)  
# entry2.place(x=200, y=315)
# btn = Button(root, text="Sign In", command=clicked, bg="white", fg="black")
# btn.place(x=200, y=400)
# root.mainloop()


# from tkinter import*
# from PIL import Image, ImageTk
# root=Tk()
# root.title("WEBSITE")
# root.geometry('1000x1000')
# root.config(bg="sky blue")
# image=Image.open("C:/Users/Cyber Security/Pictures/christmas.jpg")
# tk_image = ImageTk.PhotoImage(image)
# label_image = Label(root, image=tk_image, width=100, height=100)
# label_image.place(x=100,y=500)
# def clicked():
#     print("I am clicked")
# label_image = Label(root, image=tk_image, width=500, height=500)
# label_image.place(x=100, y=500)
# lb1 = Label(root, text="Christmas", font=("Freestyle Script", 60), bg="light yellow", fg="red")
# lb1.place(x=500, y=50)
# lb2 = Label(root, text="Username", font=("Times", "20", "bold italic"), fg="dark blue")
# lb2.place(x=25, y=200)
# entry1 = Entry(root)
# entry1.place(x=200, y=215)
# lb3 = Label(root, text="Password", font=("Times", "20", "bold italic"), fg="dark blue", bg="light yellow")
# lb3.place(x=25, y=300)
# entry2 = Entry(root)
# entry2.place(x=200, y=315)
# btn = Button(root, text="Sign In", bg="white", fg="black")
# btn.place(x=200, y=400)
# root.mainloop()
