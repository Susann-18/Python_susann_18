# class Employee:
#     def __init__(self, name, sala):
#         self.name = name
#         self.sala = sala

# # Create an instance of the Employee class
# emp = Employee("Ironman", 999000)

# # Access the sala attribute of the emp object
# print(emp.sala)

#protected

# class Employee:
#     # constructor
#     def __init__(self, name, sala):
#         self._name = name   # protected attribute 
#         self._sala = sala     # protected attribute
# emp = Employee("Captain", 10000)
# print(emp._sala)
# class HR(Employee):
    
#     # member function task
#     def task(self):
#         print ("We manage Employees")
# hrEmp = HR("Captain", 10000)
# print(hrEmp._sala)

# hrEmp.task()


 #private
# defining class Employee
# class Employee:
#     def __init__(self, name, sala):
#         self.__name = name    # private attribute 
#         self.__sala = sala      # private attribute
# emp = Employee("Bill", 10000)
# print(emp.__sala)
