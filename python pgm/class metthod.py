

# class MyClass:
#     def __init__(self, value):
#         self.value=value
#     def get_value(self):
#         return self.value
# obj=MyClass(10)
# print(obj.get_value())


# class MyClass:
#     def __init__(self,value):
#         self.value=value
#     def get_max_value(self,x,y):
#         return max(x,y)
# obj=MyClass(10)
# print(obj.get_max_value(20,30))



# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#     @staticmethod
#     def isAdult(age):
#         return age > 18
# person1 = Person('Anu',33)
# person2 = Person.fromBirthYear('Anu', 1996)
# print(person1.age)
# print(person2.age)
# print(Person.isAdult(27))

