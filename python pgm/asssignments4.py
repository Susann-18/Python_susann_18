# 1
# sum=(int(input("Enter a  number:")))
# if sum>0:
#     print("positive")
# else:
#     print("negative")
# 2
# num=(int(input("Enter a  number:")))
# if num%2==-0:
#     print("even")
# else:
#     print("odd")
# 3
# sum=(int(input("Enter a number:")))
# factorial=1
# if sum<0:
#     print("sorry,factorial negative number")
# elif sum==0:
#       print("The factorial of 0 is 1")
# else:
#      for i in range(1, sum+1):
#         factorial=factorial*i
#         print("factorial of",sum ,"is",factorial )
# 4
# num_1=10
# num_2=11
# num_3=num_1%num_2
# num_4=num_1-num_2
# num_5=num_1*num_2
# print(num_3)
# print(num_4)
# print(num_5)

# 5
# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("\n")
# asciii_n=65
# rows=4
# for i in range(0,rows):
#     for j in range(0,i+1):
#         charater=chr(asciii_n)
#         print( charater,end="")
#         asciii_n+=1
#     print("")

# 6
# str=input()
# if str==str[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# 7.
# list=[1,2,3,4,5,6]
# total=sum(list)
# print(total)

# 8
# x=(int(input("Enter a number:")))
# for n in range(1,51):
#     print(n,end="")

# 9
# num=(int(input("Enter a number:")))
# if num>1:
#     for i in range(2,sum):
#         if(num%i==0):
#             print("is not a prime number")
#             break
#         else:
#             print("is prime number")
#     else:
#         print("is not a prime number")

# 10
# num=(int(input("Enter a year:")))
# def leap_year(year):
#     if(num%4)==0:
#         if(num%100)==0:
#             if(num%400)==0:
#                 return True
#     else:
#         return False
# if leap_year(num):
#     print(f"{num} is a leap year.")
# else:
#     print(f"{num} is not a leap year.") 

# 11
# list_1=[1,2,3,4,5]
# list_2=['a','b','c','d','e']
# list=list_1+list_2
# print(list)

# 12
# x_list=[12,56,13,56,64,89,12,56,99,100]
# dict={}
# for i in x_list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# 13
# my_list = ["hello", 123, 18, "python", 34.5]
# if "python" in my_list:
#     print("'python' is present in the list")
# else:
#     print("'python' is not present in the list")

# 14
# x=(1,2,3)
# y=('a','b','c')
# z=x+y
# print("x",x)
# print("y",y)
# print("Concatenated_tuple:",z)

# 15
# my_tuple=(1,2,3,4,5,6,7,8,9)
# print(my_tuple[3:6])

# 16
# original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# swapped_dict = {value: key for key, value in original_dict.items()}
# print("Original Dictionary:", original_dict)
# print("Swapped Dictionary:", swapped_dict)


# 17
# my_list=[1,2,3,2,4,5,1,2,3,4]
# my_rem=set(my_list)
# print(my_rem)

# 18
# numbers=[]
# while True:
#     num=int(input("Enter a number (or negative number to exit):"))
#     if num<0:
#         break
#     numbers.append(num)
# for num in numbers:
#     print(num)
#     if num<0:
#         break 


# 19
# numbers=[1,2,3,4,5,6,7]
# for num in numbers:
#     print(num)
#     pass

# 20
# for num in range(1,11):
#     if num==5:
#         continue
#     print(num)