# 1
# class My_string:
#     def __init__(self):
#         self.input=""
#     def get_console(self):
#         self.input=input("Enter a string:")
#     def print_string_input_in_uppercase(self):
#         print("Uppercase version:",self.input.upper())
# x=My_string()
# x.get_console()
# x.print_string_input_in_uppercase()

# 2
# class Car:
#     def __init__(self,wheels,doors):
#         self.wheels=wheels
#         self.doors=doors
# car1=Car(4,4)
# print(car1.wheels)
# print(car1.doors)
# car2=Car(2,2)
# print(car2.wheels)
# print(car2.doors)

# 3
# class Circle():
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return self.radius**2*3.14
#     def perimeter(self):
#         return 2*self.radius*3.14
# NewCircle =Circle(8)
# print(NewCircle.area())
# print(NewCircle.perimeter())

# 4
# class Account:
#     def __init__(self):
#         self.balance=0
#         print("Your Account is created.")
#     def deposit(self):
#         amount=(int(input("Enter the amount to deposit:")))
#         self.balance+=amount
#         print('Your New Balance = ', self.balance)
#     def withdraw(self):
#         amount=(int(input('Enter the amount to withdraw:')))
#         if(amount>self.balance):

#             print('Insufficient Balance!')
#         else:
#             self.balance-=amount
#             print('Your Remaining Balance =', self.balance)
#     def enquiry(self):
#         print('Your Balance =' ,self.balance)
# account=Account()
# account.deposit()
# account.withdraw()
# account.enquiry()

# 5
# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,length):
#         super().__init__()
#         self.length=length
#     def area(self):
#         return self.length**2
# shape=Shape()
# print("Area of generic shape:",shape.area())
# square=Square(0)
# print("Area of square:",square.area())
    

