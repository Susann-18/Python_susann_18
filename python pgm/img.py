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

from tkinter import *

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if the entered username and password match predefined values
    if entered_username == "admin" and entered_password == "password":
        result_label.config(text="Login successful!", fg="green")
    else:
        result_label.config(text="Login failed. Please try again.", fg="red")

# Create main window
root = Tk()
root.title("Customized Login Page")
root.geometry("300x200")
root.config(bg="#8d1772")
# Username Label and Entry
username_label = Label(root, text="Username:",bg="#e6caf9")
username_label.pack(pady=5)

username_entry = Entry(root)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = Entry(root, show="*")  # Show '*' for password entry
password_entry.pack(pady=5)

# Login Button
login_button = Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Result Label (to display login result)
result_label = Label(root, text="",bg="#e6caf9")
result_label.pack()

root.mainloop()
