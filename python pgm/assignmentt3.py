# 1.
# x = [[12,7],
#     [4 ,5],
#     [3 ,8]]
# result=[[0,0,0],
#         [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i]=x[i][j]
# for r in result:
#  print(r)
# 2. uppercase and others to lowercase
# sentence ="I Love PYTHON"
# capitalized_string=sentence.capitalize()
# print(capitalized_string)
# 3.
# list=['maths','science',1996,1990]
# list.append(3)
# print(list)
# list1=['maths','hindi',1996,1990]
# list1.insert(2,2733)
# print(list1)
# list1=[1,2,3]
# list2=[4,5,6,7]
# list1.extend (list2)
# print(list1)
# list2.extend(list1)
# print(list2)
# List = [1, 2, 3, 4, 5]
# print(sum(List))
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(List.count(1))
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(len(List))
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(List.index(2))
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
# print(List.index(2, 2))
# numbers = [5, 2, 8, 1, 9]
# print(min(numbers))
# numbers=[5,2,8,1,9]
# print(max(numbers))
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# List.sort(reverse=True)   
# print(List)     
# list = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# print(list.pop())
# list = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# print(list.pop(0))
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# del List[0]
# print(List)
# List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
# List.remove(3)
# print(List)
# 4
# dict={1,2,3,4}
# dict1={'a','b','c','d'}
# dict.update(dict1)
# print(dict)
# 5
# my_dict={'age':56,'id':23,'name':'abc'}
# print(len(my_dict))
# print(str(my_dict))
# my_dict.keys()
# print(my_dict.keys())
# my_dict.values()
# print(my_dict.values())
# my_dict.items()
# print(my_dict.items())
# my_dict.clear()
# print(my_dict.clear())


# 6.
# list=[1,2,3,4,5]
# total=sum(list)
# print("Sum of all elements in given list:",total)
# 7
# number = int(input("Type a number: "))
# numberDict = {}
# for i in range(1, number+1):
#     numberDict[i] = i*i
# print(numberDict)
# 8.
# str =input("Input a string: ")
# d=l=0
# for c in str:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)

# 10.
# square=[]
# for i in range(10):
#     square.append(i*i)
# print(square)
# 11
# dict={'fruit':'apple','veg':'potato'}
# dict1={dict[key]:key for key in dict}
# print(dict1)

# 12.
# numbers=[9,34,11,-4,27]
# max_number=max(numbers)
# print(max_number)
# numbers=[9,34,11,-4,27]
# min_number=min(numbers)
# print(min_number)
# 13
# list=[1,2,3,4,5,6,7,8,9]
# list=[x for x in list if x%2!=0]
# print(list)

# 14
# def printvalues():
#     l=list()
#     for i in range(1,31):
#         l.append(i**2)
#     print(l)
# printvalues()
# 15
# list=["apple","orange", "cherry","dates"]
# list_1="fruit_"
# fruit_list=[list_1 + item for item in list]
# print(fruit_list)
# 16
# x=[1,2,3,4]
# y=['a','b','c','d']
# for x,y in zip(x,y):
#     print(x,y)
# 17
# my_dict={'id':24,'name':'abc','age':33}
# my_dict['company']='spectrum'
# print(my_dict)
# 18
# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50, 6:60} 
# dict4={}
# for d in (dict1,dict2,dict3):
#     dict4.update(d)
# print(dict4)
# 19
# dt={'a':'apple', 'b':'mango','c':'orange'}
# for key,value in dt.items():
#     print(key,value)
# 20
# my_dict={1:2,2:3,3:4,4:5}
# result=sum(my_dict.values())
# print(result)
# 21
# dict={'whillie':'dog','juile':'cat','lakshmi':'cow'}
# for dict_name,dict_type in dict.items():
#     print(f"{dict_name} is a {dict_type}.")
# 23
# str =input("Input a string: ")
# d={'digit':0,'letter':0}
# for c in str:
#     if c.isdigit():
#         d["digit"]+=1
#     elif c.isalpha():
#         d["letter"]+=1
#     else:
#         pass
# print("Letters", d["letter"])
# print("Digits", d["digit"])
# 24
# d=dict()
# n=10
# for x in range(1,n):
#     d[x]=x**2
# print(d)

